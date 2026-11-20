#!/usr/bin/env python3
"""Auto submit flags to CryptoHack.

Credentials are read from env vars CH_USER / CH_PASS or from a `.env` file
in the repo root (ignored by git).

Usage:
    python tools/submit.py <challenge_id> <flag>   # submit one flag
    python tools/submit.py --all                    # submit every flag in tools/flags.json
"""
import json, os, re, sys, time
from pathlib import Path
import requests

BASE = "https://cryptohack.org"
ROOT = Path(__file__).resolve().parent.parent


def load_env():
    env = ROOT / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            if "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())


def csrf(html):
    return re.search(r'_csrf_token[^>]*?value="([^"]+)"|_csrf_token: "([^"]+)"', html).group(1, 2)


def login():
    load_env()
    s = requests.Session()
    s.headers["User-Agent"] = "Mozilla/5.0"
    token = [t for t in csrf(s.get(BASE + "/login/").text) if t][0]
    r = s.post(BASE + "/login/", data={
        "username": os.environ["CH_USER"],
        "password": os.environ["CH_PASS"],
        "_csrf_token": token,
    })
    if "Incorrect username or password" in r.text:
        sys.exit("[-] Login failed: incorrect username or password")
    page = s.get(BASE + "/challenges/general/").text
    s.token = re.search(r'_csrf_token: "([^"]+)"', page).group(1)
    return s


def submit(s, cid, flag):
    r = s.post(f"{BASE}/api/submit/{cid}.json", data={"flag": flag, "_csrf_token": s.token})
    data = r.json()
    ok = not data.get("code")
    print(f"[{'+' if ok else '-'}] {cid}: {data.get('message', 'Correct!')}")
    return ok


if __name__ == "__main__":
    s = login()
    if sys.argv[1:] == ["--all"]:
        flags = json.loads((ROOT / "tools" / "flags.json").read_text())
        for cid, info in flags.items():
            submit(s, cid, info["flag"])
            time.sleep(1)
    else:
        submit(s, sys.argv[1], sys.argv[2])
