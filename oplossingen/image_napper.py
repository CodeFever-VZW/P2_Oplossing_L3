import requests

url = "https://www.shutterstock.com/_next/data/poHO5bkGMdjxHherFJviS/en/_shutterstock/search/cars.json?term=cars"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(response.status_code, response.reason)