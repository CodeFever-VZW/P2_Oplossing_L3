import requests


# HTTP requests in python
url = "https://data.stad.gent/api/explore/v2.1/catalog/datasets/real-time-bezettingen-fietsenstallingen-gent/records"

response = requests.get(url)

print(response.status_code)
print(response.reason)
print(response.json())