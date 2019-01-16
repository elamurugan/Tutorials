# from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
from urllib.request import urlopen
import sys
import re
import json

#Ask for movie title
title = input("Please enter a movie title: ")

#Ask for which year
year = input("which year? ")

#Search for spaces in the title string
raw_string = re.compile(r' ')

#Replace spaces with a plus sign
searchstring = raw_string.sub('+', title)

#Prints the search string
print(searchstring)

#The actual query
url = "http://www.json_api.com/?t=" + searchstring + "&y="+year

response = json.load(urlopen(url))

print(json.dumps(response, indent=2))