## DOWNLOAD FILE TO LOCAL MACHINE ##

from urllib import request, response
from urllib.request import urlretrieve, urlopen, Request
import pandas as pd
from bs4 import BeautifulSoup

urlretrieve('https://cdn.rebrickable.com/media/downloads/colors.csv.gz',
            '../sample-data/lego_colours.csv.gz')


## IMPORT FILE WITHOUT DOWNLOADING ##

# Read the zipped file directly into the dataframe

df = pd.read_csv('https://cdn.rebrickable.com/media/downloads/colors.csv.gz')

df.head()


## IMPORT SPREADSHEET ##

df_xls = pd.read_excel(
    'https://go.microsoft.com/fwlink/?LinkID=521962', sheet_name='Sheet1')

print(df_xls.keys())  # column names

print(df_xls[['Segment', 'Country', 'Product']].head(20))

df_xls_segment_country = df_xls[['Segment', 'Country']].drop_duplicates()
print(df_xls_segment_country)


## IMPORT HTML ##

url = 'https://therightjoin.com/about/'

request = Request(url)
response = urlopen(request)
html = response.read()

soup = BeautifulSoup(html)

print(soup.prettify())
print(soup.title)
print(soup.get_text())

response.close()
