# -*- coding: utf-8 -*-
import csv
from bs4 import BeautifulSoup
import pprint
import mechanize
import re
import os
import urllib2
import httplib
# import xlwt

# browser = mechanize.Browser()

# initialization
count_AE = 0
count_UE = 0
count_HE = 0
count_user = 0

# indicate the folder you store data in:
foldername = 'Rawdata_201607/'

# with open('babytree_user_id.csv', 'rU') as csvfile:
with open('babytree_user_id_random10.csv', 'rU') as csvfile:
	user_id_list = csv.reader(csvfile, delimiter = ';')
	for user_id_row in user_id_list:
		print '***********\nuser id: ', user_id_row
		count_page = 1
		filename = user_id_row[0] + '_post_1'
		while True:
		#if not os.path.isfile(filename):
			try:
				#count_user += 1
				url = 'http://home.babytree.com/' + user_id_row[0] + '/info/mytopic/?Ttype=post&pg=' + str(count_page)
				response = urllib2.urlopen(url)
				webcontent =  response.read()
				soup = BeautifulSoup(webcontent, "html.parser")
				tag = soup.find_all(class_="TbTab")
				# print tag
				regex = re.search(r'td(.*)class=\"TbTab\"', str(tag), re.M|re.I)
				regex = str(regex.group(1))
				print count_page
				if regex == " align=\"center\" ":
					count_user += 1
					print 'user no.: ', count_user
					print "Total number of page: ", count_page-1
					break
					#continue
				else:
					filename = foldername + user_id_row[0] + '_post_' +str(count_page)
					f = open(filename,'w')
					f.write(webcontent)
					f.close
					count_page += 1
			except AttributeError:
				count_AE += 1
				print user_id_row[0] + ' AttributeError'
				f1 = open(foldername + 'AttributeError.txt', 'a')
				f1.write(user_id_row[0] + '\n')
				f1.close
				break
				#continue
			except urllib2.HTTPError, e:
				count_UE += 1
				print user_id_row[0] + ' has been deleted'
				f = open(foldername + 'Users_not_found.txt','a')
				f.write(user_id_row[0] + '\n')
				f.close
				break
				#continue
			except httplib.BadStatusLine:
				count_HE += 1
				print user_id_row[0] + ' BadStatusLine'
				f = open(foldername + 'BadStatusLine_record.txt', 'a')
				f.write(user_id_row[0] + '\n')
				f.close
				break
				#continue
			#else:
		#	continue

print '**********************************'
print '*************Summary**************'
print '**********************************'
print 'I finished crawling ' + str(count_user) + ' users\' homepages.'
print 'Attribute Error: ' + str(count_AE)
print 'User not found: ' + str(count_UE)
print 'BadStatusLine: ' +str(count_HE)
