# ######################################################
#
# http://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html
#
# DecodeAWebPage.py
#
# Exercise 17
#
# ######################################################
#
# Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this
# website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
#
# The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that
# you can read the full article without having to click any buttons.
#
# (Hint: The post here describes in detail how to use the BeautifulSoup and requests libraries through the solution
# of the exercise posted here.)
#
# This will just print the full text of the article to the screen. It will not make it easy to read, so next exercise
# we will learn how to write this text to a .txt file.
#
# ######################################################
import requests
from bs4 import BeautifulSoup

web_page = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(web_page)
r_html = r.text
soup = BeautifulSoup(r_html, 'html.parser')

# soup = BeautifulSoup(requests.get(web_page).text, 'html.parser')

for link in soup.find_all('p'):
    for x in link.contents:
        print(x)
