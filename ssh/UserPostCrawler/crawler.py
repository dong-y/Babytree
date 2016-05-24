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

with open('babytree_user_id.csv', 'rU') as csvfile:
	user_id_list = csv.reader(csvfile, delimiter = ';')
	for user_id_row in user_id_list:
		print user_id_row
		count = 1
		while True:
			try:
				url = 'http://home.babytree.com/' + user_id_row[0] + '/info/mytopic/?Ttype=post&pg=' + str(count)
				response = urllib2.urlopen(url)
				webcontent =  response.read()
				soup = BeautifulSoup(webcontent, "html.parser")
				tag = soup.find_all(class_="TbTab")
				# print tag
				regex = re.search(r'td(.*)class=\"TbTab\"', str(tag), re.M|re.I)
				regex = str(regex.group(1))
				print count
				if regex == " align=\"center\" ":
					print "Total number of page: ", count-1
					break
				else:
					f = open(user_id_row[0] + '_post_' + str(count),'w')
					f.write(webcontent)
					f.close
			except AttributeError:
				print user_id_row[0] + ' AttributeError'
				f1 = open('AttributeError', 'a')
				f1.write(user_id_row[0] + '\n')
				f1.close
				break
			except urllib2.HTTPError, e:
				print user_id_row[0] + ' has been deleted'
				f = open('users_not_found','a')
				f.write(user_id_row[0] + '\n')
				f.close
				break
			except httplib.BadStatusLine:
				print user_id_row[0] + ' BadStatusLine'
				f = open('BadStatusLine_record', 'a')
				f.write(user_id_row[0] + '\n')
				f.close
				break
			count += 1
