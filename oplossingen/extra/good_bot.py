import requests

url = "https://www.shutterstock.com/_next/data/poHO5bkGMdjxHherFJviS/en/_shutterstock/search/cars.json?term=cars"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}


def is_good_or_bad_bot(json):
    is_good_bot = json["botProps"]["isGoodBot"]
    is_suspected_bad_bot = json["botProps"]["isSuspectedBadBot"]
    print(f"Is good bot? {is_good_bot}")
    print(f"Is suspected bad bot? {is_suspected_bad_bot}")


response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(response.status_code)
    data = None

if data is None:
    print('no data received')
else:
    is_good_or_bad_bot(data)