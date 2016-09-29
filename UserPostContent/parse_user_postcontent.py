# -*- coding: utf-8 -*-
import os
from bs4 import BeautifulSoup
import codecs
import re
import csv
import urllib2
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')
# import bleach

# f2 = codecs.open('babytree_user_post_content_only.csv','a', 'utf-8')
count = 0

f = open('babytree_user_post_content.csv','w')
f.write('user_id;url;title;postcontent\n')
f.close()

with open('babytree_user_post_url.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter = ';')
	for row in reader:
		count += 1
		print count
		user_id = row[0]
		title = row[5]
		url = row[6]
		# url = "http://www.babytree.com/community/group27063/topic_12114134.html"
		filename = url.replace('/','_').replace(':','_').replace('.','_')
		if os.path.isfile(filename):
			f = open(filename, 'r')
			soup = BeautifulSoup(f, 'html.parser')
			try:
				tag = soup.find(id = 'topic_content').stripped_strings
				postcontent = []
				# for string in tag:
				# 	print(string)
				postcontent = ''.join(tag)
				postcontent = postcontent.replace('\n','').replace(' ','')
				print postcontent
				# f = codecs.open('000000000000.csv','a', 'utf-8')
				f = codecs.open('babytree_user_post_content.csv','a', 'utf-8')
				f.write(user_id + ';' + url + ';' + title + ';' + postcontent + '\n')
				f.close()
				# f2.write(url + ';' postcontent + ';\n')
				# f2.close()
			except AttributeError:
				print url + ' AttributeError'
				f = open('attributeerror_parsing.txt','a')
				f.write(url + '\n')
				f.close()
		else:
			print url + ' file does not exist'
			f = open('ioerror_parsing.txt','a')
			f.write(url + '\n')
			f.close()


