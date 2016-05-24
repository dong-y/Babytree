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
		# url = "http://www.babytree.com/community/group27063/topic_12114134.html"
		filename = url.replace('/','_').replace(':','_').replace('.','_')
		f = open(filename, 'r')
		soup = BeautifulSoup(f, 'html.parser')
		tag = soup.find(id = 'topic_content').stripped_strings
		postcontent = []
		# for string in tag:
		# 	print(string)
		postcontent = ''.join(tag)
		postcontent = postcontent.replace('\n','').replace(' ','')
		print postcontent
		f = codecs.open('babytree_user_post_content.csv','a', 'utf-8')
		# f = codecs.open('000000000000.csv','a', 'utf-8')
		f.write(user_id + ';' + url + ';' + postcontent + ';\n')
		# f.write(postcontent)
		f.close()

