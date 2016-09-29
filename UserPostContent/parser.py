# -*- coding: utf-8 -*-
import os
from bs4 import BeautifulSoup
import codecs
import re
import csv
import urllib2
from datetime import datetime

# reload(sys)  
# sys.setdefaultencoding('utf8')

count = 0

# initiate the output files:
f = open('babytree_user_post_content.csv','w') #########################
f.write('user_id;url;title;body\n')
f.close()

# indicate the input and output folder
# YYYYMM = datetime.now().strftime("%Y%m")
YYYYMM = '201607'
inputdir = 'Input_' + YYYYMM + '/'
rawdir = 'Rawdata_' + YYYYMM + '/'
outputdir = 'Output_' + YYYYMM + '/'
#crawlerdir = '../UserPostCrawler/Output_' + YYYYMM + '/' # the file to be parsed is stored in the UserPostCrawler dir

# delete the output files if they ever exist
out_tb = outputdir + 'babytree_user_post_content.csv'
out_t = outputdir + 'babytree_user_post_title.csv'
out_b = outputdir + 'babytree_user_post_title.csv'
outputfs = [out_tb, out_t, out_b]

for f in outputfs:
	if os.path.exists(f):
   		os.remove(f)

def find_title(htmltag):
	title = htmltag.find('a').get('title')
	print 'title = ', title
	return title

def find_body(htmlpage):
	tag = htmlpage.find(id = 'topic_content').stripped_strings
	body = []
	body = ''.join(htmltag)
	body = body.replace('\n','').replace(' ','')
	return body

def find_date(htmltag):
	return date

def find_user_info(html):


with open(inputdir + 'babytree_user_post_url.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter = ';')
	for row in reader:
		count += 1
		print count
		user_id = row[0]
		url = row[4]
		filename = url.replace('/','_').replace(':','_').replace('.','_')
		print filename #############
		if os.path.isfile(rawdir + filename):
			print 'hi!'
			f = open(rawdir + filename, 'r')
			webpage = BeautifulSoup(f, 'html.parser')
			try:
				body = find_body(webpage)
				title = webpage.title.string
				print body
				f = codecs.open(out_tb,'a', 'utf-8')
				f.write(user_id + ';' + url + ';' + title + ';' + body + '\n')
				f.close()
				f1 = codecs.open(out_b,'a','utf-8')
				f1.write(user_id + ';' + url + ';' + body + '\n')
				f1.close()
				f2 = codecs.open(out_t,'a','utf-8')
				f2.write(user_id + ';' + url + ';' + title + '\n')
				f2.close()
				break ##################
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

