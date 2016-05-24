# -*- coding: utf-8 -*-
import os
from bs4 import BeautifulSoup
import codecs
import re
import csv
import urllib2
import bleach

with open('babytree_user_post_url.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter = ';')
	for row in reader:
		user_id = row[0]
		url = row[6]
		filename = "http___www_babytree_com_community_zaojiao_topic_32663423_html"
		# filename = url.replace('/','_').replace(':','_').replace('.','_')
		f = open(filename, 'r')
		soup = BeautifulSoup(f, 'html.parser')
		tag = soup.find(id = 'topic_content').stripped_strings
		for string in tag:
			clean = bleach.delinkify(soup,tags[],strip=True)
