import requests
import json

url = "https://gg.asuracomic.net/api/reader/6067/chapter/259518"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://asuracomic.net/",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)
print(json.dumps(response.json(), indent=2))
