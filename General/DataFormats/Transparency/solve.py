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
