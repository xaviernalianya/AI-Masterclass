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