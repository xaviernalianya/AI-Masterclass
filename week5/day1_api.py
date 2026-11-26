import requests

url = "https://restcountries.com/v5/name/kenya?fields=name,capital,population,currencies"

response = requests.get(url)

data= response.json()
print(data)