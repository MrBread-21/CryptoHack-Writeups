# Transparency

**Category:** General / Data Formats · **Points:** 50

**Challenge files:** [`transparency.pem`](transparency.pem)

## Idea

Every TLS certificate must be published to Certificate Transparency logs. crt.sh lets us search logs by the SHA256 of the public key (`spkisha256`).
Hash the DER `SubjectPublicKeyInfo` of the given key, look it up on crt.sh, read the domain from the certificate (`thetransparencyflagishere.cryptohack.org`) and visit it to get the flag.

## Solution

```python
import hashlib, re, requests
from Crypto.PublicKey import RSA

# 1. Search Certificate Transparency logs (crt.sh) by SHA256 of the public key
spki = RSA.import_key(open("transparency.pem").read()).export_key("DER")
cert_id = requests.get(f"https://crt.sh/?spkisha256={hashlib.sha256(spki).hexdigest()}&output=json").json()[0]["id"]

# 2. Read the domain name from that certificate
domain = re.search(r"[\w.-]+\.cryptohack\.org", requests.get(f"https://crt.sh/?id={cert_id}").text).group()
print(domain)

# 3. Visit the subdomain
print(re.search(r"crypto\{.*?\}", requests.get(f"https://{domain}").text).group())
#crypto{thx_redpwn_for_inspiration}
```

## Flag

```text
crypto{thx_redpwn_for_inspiration}
```
