import requests

url = "https://asurascans.com/api/chapter/sword-gods-livestream/23"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://asurascans.com/",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)
print("Status:", response.status_code)
print("Response:", response.text[:500])
