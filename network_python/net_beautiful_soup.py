from urllib import request, parse, error
from bs4 import BeautifulSoup

url = input('Enter - ') # ask for input of a website to scrap
html = request.urlopen(url).read() # read the url(varible) ## data should not be large
soup = BeautifulSoup(html, 'html.parser') # so BeautifulSoup takes html and tears is apart 

# Retrieve all of the acnchor tags

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))