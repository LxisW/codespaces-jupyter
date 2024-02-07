import requests, time
from datetime import datetime


headers = {
    "authority": "api.coinbase.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "max-age=0",
    "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
}


crypto = "BTC"
response = requests.get(
    f"https://api.coinbase.com/v2/exchange-rates?currency={crypto}",
    headers=headers,
)
print(response.url)
data = response.json()["data"]["rates"]
currency = "EUR"
if currency in data:
    price_eur = data[currency]

print(
    f"The price of {crypto} is {price_eur}{currency} at {datetime.now().strftime('%d.%m.%Y %H:%M')}"
)
