# -*- coding: utf-8 -*-
import os
from bs4 import BeautifulSoup
import codecs
import re
import csv
import urllib2
from datetime import datetime

# the input and output folder
YYYYMM = '201607'
# YYYYMM = datetime.now().strftime("%Y%m")
inputdir = 'Input_' + YYYYMM + '/'
rawdir = 'Rawdata_' + YYYYMM + '/'
outputdir = 'Output_' + YYYYMM + '/'

# initiate count
count = 0
count_othererror = 0
count_404 = 0
count_badstatusline = 0
count_attri = 0
count_crawled = 0

f1 = open(inputdir + 'Users_not_found.txt','r')
urls_404 = f1.readlines()
f1.close

# f2 = open(inputdir + 'AttributeError.txt','r')
# urls_ae = f2.readlines()

# f2 = open(outputdir + 'BadStatusLine_record.txt', 'w')
# urls_badstatus = f2.readlines()

with open(inputdir + 'babytree_user_post_url.csv', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter = ';')
	for row in reader:
		user_id = row[0]
		# url = row[6]
		url = row[4]
		urltemp = url + '\n'
		count += 1
		print 'count =', count
		if urltemp in urls_404:
			count_404 += 1
			print url, ' 404'
		# elif urltemp in urls_badstatus:
		# 	count_badstatusline += 1
		# 	print url, ' BadStatusLine'
		else:
			filename = rawdir + url.replace('/','_').replace(':','_').replace('.','_')
			if os.path.isfile(filename):
				count_crawled += 1
				print url, 'crawled'
				pass
			else:
				try:
					response = urllib2.urlopen(url)
					webcontent =  response.read()
					print filename
					f = open(filename, 'w')
					f.write(webcontent)
					f.close()
					count_crawled += 1
				except AttributeError:
					count_attri += 1
					print url + ' AttributeError'
					f = open(outputdir + 'AttributeError.txt', 'a')
					f.write(url + '\n')
					f.close
					continue
				# except urllib2.HTTPError, e:
				# 	print url + ' has been deleted'
				# 	f = open('users_not_found.txt','a')
				# 	f.write(url + '\n')
				# 	f.close
				# 	continue
				# except httplib.BadStatusLine:
				# 	print url + ' BadStatusLine'
				# 	f = open('BadStatusLine_record.txt', 'a')
				# 	f.write(url + '\n')
				# 	f.close			
				# 	continue
				except:
					count_othererror += 1 
					print "other errors"
					continue

count_error = count_404 + count_badstatusline + count_attri + count_othererror

count_left = count - count_crawled - count_error

# f2.close
print '**********************\nProgress Summary'
print 'Time: ', str(datetime.now())
print 'Count: total = %d, crawled = %d, left = %d, error = %d ' %(count, count_crawled, count_left, count_error)
print 'Error count: 404 = %d, BadStatusLine = %d, othererror = %d, AttributeError = %d' %(count_404, count_badstatusline, count_othererror, count_attri)
print 'Details: babytree_user_post_crawler_process.csv'
# print 'To be crawled: babytree_user_post_url_left.csv\n'
