# ######################################################
#
# http://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html
# DecodeAWebPage.py
#
# Exercise 17
#
# ######################################################
#
# Use the BeautifulSoup and requests Python packages to print out a list of all the article
# titles on the New York Times homepage.
#
# ######################################################
import requests
from bs4 import BeautifulSoup

web_page = "https://www.nytimes.com"
r = requests.get(web_page)
r_html = r.text
soup = BeautifulSoup(r_html, 'html.parser')

for link in soup.find_all('h2'):
    if link.contents[0].name == 'a':
        headline = link.contents[0].string
        if headline is not None:
            print(headline)
