#!/usr/bin/env python3
"""Auto submit flags to CryptoHack.

Credentials are read from env vars CH_USER / CH_PASS or from a `.env` file
in the repo root (ignored by git). The login session is cached in `.ch_session`.

Usage:
    python tools/submit.py <challenge_id> <flag>   # submit one flag
    python tools/submit.py --all                    # submit every flag in tools/flags.json
"""
import json, os, pickle, re, sys, time
from pathlib import Path
import requests

BASE = "https://cryptohack.org"
ROOT = Path(__file__).resolve().parent.parent
SESSION_FILE = ROOT / ".ch_session"


def load_env():
    env = ROOT / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            if "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())


def post(s, url, data):
    """POST and wait/retry when CryptoHack says we are too fast."""
    while True:
        r = s.post(url, data=data)
        if "doing that too fast" not in r.text:
            return r
        print("[*] Rate limited, waiting 30s...")
        time.sleep(30)


def get_token(s):
    """Return the CSRF token if the session is logged in, else None."""
    m = re.search(r'_csrf_token: "([^"]+)"', s.get(BASE + "/challenges/general/").text)
    return m and m.group(1)


def login():
    load_env()
    s = requests.Session()
    s.headers["User-Agent"] = "Mozilla/5.0"
    if SESSION_FILE.exists():
        s.cookies.update(pickle.loads(SESSION_FILE.read_bytes()))
        s.token = get_token(s)
        if s.token:
            return s
    page = s.get(BASE + "/login/").text
    token = re.search(r'name="_csrf_token" type="hidden" value="([^"]+)"', page).group(1)
    r = post(s, BASE + "/login/", {
        "username": os.environ["CH_USER"],
        "password": os.environ["CH_PASS"],
        "_csrf_token": token,
    })
    if "Incorrect username or password" in r.text:
        sys.exit("[-] Login failed: incorrect username or password")
    s.token = get_token(s)
    if not s.token:
        sys.exit("[-] Login failed")
    SESSION_FILE.write_bytes(pickle.dumps(s.cookies))
    return s


def submit(s, cid, flag):
    data = post(s, f"{BASE}/api/submit/{cid}.json", {"flag": flag, "_csrf_token": s.token}).json()
    msg = data.get("message", "Correct!")
    ok = not data.get("code") or "already solved" in msg
    print(f"[{'+' if ok else '-'}] {cid}: {msg}")
    return ok


if __name__ == "__main__":
    s = login()
    if sys.argv[1:] == ["--all"]:
        flags = json.loads((ROOT / "tools" / "flags.json").read_text(encoding="utf8"))
        for cid, info in flags.items():
            submit(s, cid, info["flag"])
            time.sleep(1)
    else:
        submit(s, sys.argv[1], sys.argv[2])
