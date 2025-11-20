import requests
import sys
def get_title(artist):
    try:
        response = requests.get("https://api.artic.edu/api/v1/artworks/search",{'q':artist})
        response.raise_for_status()
    except requests.HTTPError:
        sys.exit()
    response = response.json()
    for name in response['data']:
        print(name['title'])
