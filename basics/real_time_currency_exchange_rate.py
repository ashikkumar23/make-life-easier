#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# Created On  : macOS Catalina 10.15.7 (19H15)
# Created On  : Python 3.8.2
# Created By  : Ashik Kumar
# Created Date: Sat, Nov 13 2021 18:15:00 IST
# -----------------------------------------------------------------------------
"""THE MODULE HAS BEEN BUILT FOR GETTING THE REAL TIME CURRENCY EXCHANGE RATE"""
# -----------------------------------------------------------------------------

import requests
import constants
from typing import Dict

# Get your free API Key from https://www.alphavantage.co/support/#api-key and save it in `constants.py` file
# Example: API_KEY = "<your_api_key>"
API_KEY = constants.API_KEY
BASE_URL = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"


class RealTimeCurrencyExchangeRate:
    def __init__(self, from_currency: str, to_currency: str, api_key: str) -> None:
        self.from_currency = from_currency.upper()
        self.to_currency = to_currency.upper()
        self.api_key = api_key

    def get_exchange_rate(self) -> Dict:
        url = f"{BASE_URL}&from_currency={self.from_currency}&to_currency={self.to_currency}&apikey={self.api_key}"
        response = requests.get(url).json()
        if "Realtime Currency Exchange Rate" not in response:
            raise ValueError("Invalid currency code(s). Please check and try again.")
        return response

    def convert(self) -> None:
        try:
            response = self.get_exchange_rate()
            exchange_rate = response["Realtime Currency Exchange Rate"]
            from_cur_name = exchange_rate["2. From_Currency Name"]
            to_cur_name = exchange_rate["4. To_Currency Name"]
            rate = exchange_rate["5. Exchange Rate"]
            print(
                f"\nRealtime Currency Exchange Rate: 1 {from_cur_name} Equals {rate} {to_cur_name}"
            )
        except (ValueError, requests.exceptions.RequestException) as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    while True:
        # Get the list of currency codes from https://simple.wikipedia.org/wiki/ISO_4217#Official_codes
        from_cur = input('Enter "From Currency" Code: ')  # Example: "USD"
        to_cur = input('Enter "To Currency" Code: ')  # Example: "INR"
        if len(from_cur) != 3 or len(to_cur) != 3:
            print("Invalid currency code(s). Please try again.")
            continue
        RealTimeCurrencyExchangeRate(from_cur, to_cur, API_KEY).convert()
        break
