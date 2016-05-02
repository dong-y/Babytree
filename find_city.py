
import os
from natsort import natsorted
from bs4 import BeautifulSoup
import codecs
import networkx as nx
import re


def find_city_from_li_from_post_div(htmlfile):
	soup = BeautifulSoup(htmlfile, 'html.parser')
	tag = soup.find_all('ul', class_="userProfileDetail")
	print tag[0]
	city = re.search(r'<a target="_blank" rel="nofollow" href="http://(.*).city.babytree.com/">', str(tag[0]), re.M|re.I)
	print city
	city_str = str(city.group(1))
	# print 'city_str is ' + city_str
	return city_str

filename = "www.babytree.com_community_club000000_topic_2171111_1.html.txt"
f = open(filename,'r')
city = find_city_from_li_from_post_div(f)
print "city is " + city
f.close()