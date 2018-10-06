#!/usr/bin/env python
"""
Script to print
 - Size of the webpage in bytes
 - Number of links in that page pointing to same domain (find <a> tags)
"""
import urllib.request
import requests
from bs4 import BeautifulSoup

URL = input("Enter URL of webpage: ")    		# Take any URL as input

SLASHPARTS = URL.split('/')        # split the URL with /
"""
 BASENAME: contains the URL of the original domain of the page eg. "http://www.example.com/"
"""
BASENAME = '/'.join(SLASHPARTS[:3]) + '/'

GETPAGE = requests.get(URL)

PAGE = urllib.request.urlopen(URL)

SOUP = BeautifulSoup(GETPAGE.text, 'html.parser')

print("____________________________________________")
print("Size: ", len(PAGE.read()), "bytes")		# prints the size of the webpage

ALL_LINKS = SOUP.findAll('a')

COUNT = 0

for link in ALL_LINKS:
    if link.get('href') == BASENAME:
        COUNT += 1

print("<a> tags: ", COUNT)
