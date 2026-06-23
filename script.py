import requests
import json

url = "https://asurascans.com/api/chapter/sword-gods-livestream/23"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://asuracomic.net/",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)
print(json.dumps(response.json(), indent=2))
