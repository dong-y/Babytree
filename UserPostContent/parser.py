# -*- coding: utf-8 -*-
import os
from bs4 import BeautifulSoup
import codecs
import re
import csv
import urllib2
from datetime import datetime

reload(sys)  
sys.setdefaultencoding('utf8')

count = 0

# initiate the output files:
f = open('babytree_user_post_content.csv','w')
f.write('user_id;url;title;body\n')
f.close()

# indicate the input and output folder
# YYYYMM = datetime.now().strftime("%Y%m")
YYYYMM = '201607'
inputdir = 'Input_' + YYYYMM + '/'
rawdir = 'Rawdata_' + YYYYMM + '/'
outputdir = 'Output_' + YYYYMM + '/'

with open(inputdir + 'babytree_user_post_url.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter = ';')
	for row in reader:
		count += 1
		print count
		user_id = row[0]
		url = row[4]
		filename = url.replace('/','_').replace(':','_').replace('.','_')
		if os.path.isfile(filename):
			f = open(rawdir + filename, 'r')
			soup = BeautifulSoup(f, 'html.parser')
			try:
				tag = soup.find(id = 'topic_content').stripped_strings
				body = []
				body = ''.join(tag)
				body = body.replace('\n','').replace(' ','')
				print body
				f = codecs.open(outputdir + 'babytree_user_post_content.csv','a', 'utf-8')
				f.write(user_id + ';' + url + ';' + title + ';' + body + '\n')
				f.close()
				f1 = codecs.open(outputdir + 'babytree_user_post_title.csv','a','utf-8')
				f1.write(user_id + ';' + url + ';' + body + '\n')
				f1.close()
				f2 = codecs.open(outputdir + 'babytree_user_post_title.csv','a','utf-8')
				f2.write(user_id + ';' + url + ';' + title + '\n')
				f2.close()
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

