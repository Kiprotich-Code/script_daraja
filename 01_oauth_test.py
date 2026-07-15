import requests
import base64
import json

# ==============================
# CONFIG
# ==============================

ENVIRONMENT = "sandbox"

CONSUMER_KEY = ""
CONSUMER_SECRET = ""

BASE_URL = (
    "https://sandbox.safaricom.co.ke"
    if ENVIRONMENT == "sandbox"
    else "https://api.safaricom.co.ke"
)

# ==============================
# REQUEST TOKEN
# ==============================

auth = base64.b64encode(
    f"{CONSUMER_KEY}:{CONSUMER_SECRET}".encode()
).decode()

headers = {
    "Authorization": f"Basic {auth}"
}

url = (
    f"{BASE_URL}/oauth/v1/generate"
    "?grant_type=client_credentials"
)

try:

    print("Requesting OAuth token...\n")

    response = requests.get(
        url,
        headers=headers,
        timeout=30
    )

    print("Status:", response.status_code)
    print()

    print(json.dumps(response.json(), indent=4))

    response.raise_for_status()

    print("\nSUCCESS")

except Exception as e:
    print(e)
