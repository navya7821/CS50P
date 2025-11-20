import requests
import sys

if len(sys.argv) == 1:
    sys.exit('Missing command-line argument')

try:
    number = float(sys.argv[1])
except ValueError:
    sys.exit('Command-line argument is not a number')
response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
response = response.json()
det = response['data']
price = det['priceUsd']
price = float(price)
cost = number * price
print(f'${cost:,.4f}')


