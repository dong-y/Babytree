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
		print ','.join(user_id_row)
		try:
			response = urllib2.urlopen('http://home.babytree.com/' + user_id_row[0])
			webContent = response.read()
			f = open(user_id_row[0],'w')
			f.write(webContent)
			f.close
		except urllib2.HTTPError, e:
			print user_id_row[0] + ' has been deleted'
			f = open('users_not_found','a')
			f.write(user_id_row[0] + '\n')
			f.close
			continue
		except httplib.BadStatusLine:
			print user_id_row[0] + ' BadStatusLine'
			f = open('BadStatusLine_record', 'a')
			f.write(user_id_row[0] + '\n')
			f.close
			pass