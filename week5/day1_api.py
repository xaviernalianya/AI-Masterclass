import requests

url = "https://restcountries.com/v3.1/name/kenya"

response = requests.get(url)

print("Status code:", response.status_code)
print("Data received:", response.json())