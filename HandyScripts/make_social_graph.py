from bs4 import BeautifulSoup
import pprint
import mechanize
import re
import os

browser = mechanize.Browser()

html_file = open('/Users/dong/Downloads/link_1_1.txt', 'r')
soup = BeautifulSoup(html_file.read())
html_file.close()