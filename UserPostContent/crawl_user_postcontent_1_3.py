# -*- coding: utf-8 -*-
import os
from bs4 import BeautifulSoup
import codecs
import re
import csv
import urllib2
import httplib
from socket import error as SocketError
import errno
from multiprocessing import Pool

def show_video_stats(options):
    pool = Pool(8)
    video_page_urls = get_video_page_urls()
    results = pool.map(get_video_data, video_page_urls)


# with open('babytree_user_post_url.csv', 'r') as csvfile:
# 	with open('babytree_user_post_content.csv', 'r') as csvoutput:
# 		writer = csv.writer(csvoutput, encoding='utf-8', delimiter = ';', lineterminator = '\n')
# 		reader = csv.reader(csvfile, encoding='utf-8', delimiter = ';')
		
# 		all = []
# 		row = next(reader)
# 		all.append(row)

# 		for row in reader:
# 			user_id = row[0]
# 			url = row[6]
# 			response = urllib2.urlopen(url)
# 			webcontent =  response.read()
# 			soup = BeautifulSoup(webcontent, "html.parser")
# 			topic_content = soup.find(id = 'topic_content')
# 			row.append(topic_content)
# 			all.append(row)

# 		writer.writerows(all)

# def cleanline(string):
# 	print string
# 	newstring = string.replace('\n','...')
# 	newstring = string.replace(' ','')
# 	print "***********\n", newstring
# 	return newstring

with open('babytree_user_post_url_1_3.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter = ';')
	for row in reader:
		user_id = row[0]
		url = row[6]
		filename = url.replace('/','_').replace(':','_').replace('.','_')
		if not os.path.isfile(filename):
			try:
				response = urllib2.urlopen(url)
				webcontent =  response.read()
				# soup = BeautifulSoup(webcontent, "html.parser")
				# content = soup.find(id = 'topic_content')
				# content = []	
				# for string in soup.find(id = 'topic_content').strings:
				# 	print(repr(string))
				# 	content = ''.join(repr(string))
				# print type(content)
				# content_clean = bleach.delinkify(content)
				# print user_id, url, content
				# print topic_content
				# print "****************"
				# topic_content = cleanline(topic_content)
				print(filename)
				# f = codecs.open(filename,'a', 'utf-8')
				f = open(filename, 'w')
				# f.write(user_id + ';' + url + ';' + content + ';\n')
				f.write(webcontent)
				f.close()
			except AttributeError:
				print url + ' AttributeError'
				f1 = open('AttributeError.txt', 'a')
				f1.write(url + '\n')
				f1.close
				continue
			except urllib2.HTTPError, e:
				print url + ' has been deleted'
				f = open('users_not_found.txt','a')
				f.write(url + '\n')
				f.close
				continue
			except httplib.BadStatusLine:
				print url + ' BadStatusLine'
				f = open('BadStatusLine_record.txt', 'a')
				f.write(url + '\n')
				f.close
				continue
			except:
				print url + 'other errors'
				f = open('othererror.text', 'a')
				f.write(url + '\n')
				f.close
				# some or all of the counters could not be scraped
				continue
		else:
			continue







