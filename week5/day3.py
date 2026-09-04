#API Keys and Authentication
# This is a sample of how to use the X API v2 with Python
import os

# Simulate: load key from environment
os.environ["SMP_API_KEY"] = "smp_live_abc123xyz"
api_key = os.getenv("SMP_API_KEY")

# Build request components (what you would pass to requests.get)
url = "https://api.smptracker.com/v1/members"
params = {"city": "Nairobi", "limit": 10}
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

print("URL:", url)
print("Params:", params)
print("Auth header:", "Bearer " + api_key[:8] + "...")

# Simulate a 200 response
print()
print("Response status: 200")
print("Response body: { 'members': [...], 'total': 42 }")

#Error Handling
def handle_api_response(status_code, body):
    if status_code == 200:
        return body
    elif status_code == 401:
        raise PermissionError("Authentication failed. Check your API key.")
    elif status_code == 403:
        raise PermissionError("Access denied. Your key does not have permission for this endpoint.")
    elif status_code == 429:
        raise RuntimeError("Rate limit exceeded. Wait before retrying.")
    elif status_code >= 500:
        raise RuntimeError(f"Server error ({status_code}). Try again later.")
    else:
        raise RuntimeError(f"Unexpected status: {status_code}")

# Test with different status codes
test_cases = [
    (200, {"members": [{"name": "James Omondi"}]}),
    (401, {"error": "invalid_key"}),
    (429, {"error": "rate_limit_exceeded"}),
    (500, {"error": "internal_server_error"}),
]

for status, body in test_cases:
    try:
        result = handle_api_response(status, body)
        print(f"Status {status}: OK, got {result}")
    except Exception as e:
        print(f"Status {status}: {e}")


        #The same authentication pattern applies to every business API in Kenya. 
        # The Safaricom M-Pesa Daraja API requires a Consumer Key and Consumer Secret. 
        # You exchange them for a Bearer token, then use that token on every transaction call. 
  
        # Farms, agro-dealers, and small businesses that accept M-Pesa payments build on top of this exact flow.
import os
import base64

# Step 1: Load credentials from environment (never hardcode)
os.environ["MPESA_CONSUMER_KEY"]    = "demo_consumer_key_abc123"
os.environ["MPESA_CONSUMER_SECRET"] = "demo_secret_xyz789"

consumer_key    = os.getenv("MPESA_CONSUMER_KEY")
consumer_secret = os.getenv("MPESA_CONSUMER_SECRET")

# Step 2: Encode credentials (Daraja requires Base64)
credentials = f"{consumer_key}:{consumer_secret}"
encoded = base64.b64encode(credentials.encode()).decode()

# Step 3: In production you POST this to Daraja to get a token:
#   url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
#   headers = {"Authorization": f"Basic {encoded}"}
#   response = requests.get(url, headers=headers)
#   token = response.json()["access_token"]

# Simulate the token response
simulated_token = "Q2xpZW50X0lENmJlYjA2NWEtMjA4Ny00OTU2"

print("Credentials encoded (Base64):", encoded[:20] + "...")
print()
print("Simulated token received:", simulated_token[:20] + "...")
print()
print("In production, pass this token to every M-Pesa API call:")
print(f'  headers = {{"Authorization": "Bearer {simulated_token[:12]}..."}}')
print()
print("Example endpoint: STK Push (prompt customer to pay)")
print("  POST https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest")