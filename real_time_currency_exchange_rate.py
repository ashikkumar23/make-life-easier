#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# Created On  : macOS Catalina 10.15.7 (19H15)
# Created On  : Python 3.8.2
# Created By  : Ashik Kumar
# Created Date: Sat, Nov 13 2021 18:15:00 IST
# -----------------------------------------------------------------------------
"""THE MODULE HAS BEEN BUILT FOR GETTING THE REAL TIME CURRENCY EXCHANGE RATE"""
# -----------------------------------------------------------------------------

import json
import requests
import constants


class RealTimeCurrencyExchangeRate:
    def __init__(self, from_currency, to_currency, api_key):
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.api_key = api_key

    def convert(self):
        base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
        main_url = base_url + "&from_currency=" + self.from_currency + "&to_currency=" + self.to_currency + "&apikey=" + self.api_key
        response = requests.get(main_url).json()
        print("\nBefore parsing:", "\n" + json.dumps(response, indent=4))
        print("\nAfter parsing:" + "\n" + "Realtime Currency Exchange Rate: 1",
              response["Realtime Currency Exchange Rate"]["2. From_Currency Name"], "Equals",
              response["Realtime Currency Exchange Rate"]['5. Exchange Rate'],
              response["Realtime Currency Exchange Rate"]["4. To_Currency Name"])


if __name__ == "__main__":
    # Get the list of currency codes from https://simple.wikipedia.org/wiki/ISO_4217#Official_codes
    from_cur = input('Enter "From Currency" Code: ').upper()  # Example: "USD"
    to_cur = input('Enter "To Currency" Code: ').upper()  # Example: "INR"
    RealTimeCurrencyExchangeRate(from_cur, to_cur, constants.API_KEY).convert()
