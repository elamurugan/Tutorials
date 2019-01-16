from bs4 import BeautifulSoup

import requests
import sys

url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print('IMDB Top Rated Movies')
getTr = soup.findChildren("tr")
trList = iter(getTr)
next(trList)
for tr in trList:
    # print('TR Row:')
    # print(tr)
    title = tr.find('td', {'class': 'titleColumn'}).find('a').contents[0]
    year = tr.find('td', {'class': 'titleColumn'}).find('span', {'class': 'secondaryInfo'}).contents[0]
    rating = tr.find('td', {'class': 'ratingColumn imdbRating'}).find('strong').contents[0]
    movie = title + ' - ' + year + ' ' + ' ' + rating
    print('Movie => ' + movie)