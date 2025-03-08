import sys
import requests



try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    if sys.argv[1].isalpha():
        sys.exit("Missing command-line argument")
    else:
        o = requests.get("https://api.coincap.io/v2/assets/bitcoin")
        info = o.json()
        x = info["bpi"]["USD"]["rate_float"]
        total = float(x) * float(sys.argv[1])
        print(f"${total:,.4f}")
except requests.RequestException:
    pass