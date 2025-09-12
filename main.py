# Crypto Price Tracker
# Author: Med Amine
# Description: Fetches real-time crypto prices using CoinGecko API

import requests

def get_price(coin_id, currency="usd"):
    """
    Fetch current price of a cryptocurrency from CoinGecko
    """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data[coin_id][currency]
    else:
        print("⚠️ Error fetching data")
        return None


if __name__ == "__main__":
    print("💰 Crypto Price Tracker 💰")
    coins = ["bitcoin", "ethereum", "dogecoin"]

    for coin in coins:
        price = get_price(coin)
        if price is not None:
            print
