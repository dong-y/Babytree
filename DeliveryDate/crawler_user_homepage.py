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

# indicate the input and output folder
YYYYMM = datetime.now().strftime("%Y%m")
inputdir = 'Input_' + YYYYMM + '/'
rawdir = 'Rawdata_' + YYYYMM + '/'
outputdir = 'Output_' + YYYYMM + '/'

with open(inputdir + 'babytree_user_id_random10.txt', 'rU') as csvfile:
	user_id_list = csv.reader(csvfile, delimiter = ',')
	for user_id_row in user_id_list:
		print ','.join(user_id_row)
		try:
			response = urllib2.urlopen('http://home.babytree.com/' + user_id_row[0] + '/growth')
			webContent = response.read()
			f = open(rawdir + user_id_row[0],'w')
			f.write(webContent)
			f.close
		except urllib2.HTTPError, e:
			print user_id_row[0] + ' has been deleted'
			f = open(outputdir + 'User_not_found.txt','a')
			f.write(user_id_row[0] + '\n')
			f.close
			continue
		except httplib.BadStatusLine:
			print user_id_row[0] + ' BadStatusLine'
			f = open(outputdir + 'BadStatusLine_record.txt', 'a')
			f.write(user_id_row[0] + '\n')
			f.close
			pass
