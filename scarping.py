import pandas as pd 
import requests 
from io import StringIO

URL = 'https://en.wikipedia.org/wiki/List_of_largest_banks'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(URL, headers=headers)
response.raise_for_status()  # raises error if still blocked

html = StringIO(response.text)
tables = pd.read_html(html)

print(tables[0])

#print(tables[0])
#URL = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
#tables = pd.read_html(URL)
#df = tables[0]
#print(df)
