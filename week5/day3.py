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