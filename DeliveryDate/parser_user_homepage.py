# -*- coding: UTF-8 -*-
import os
from natsort import natsorted
from bs4 import BeautifulSoup
import codecs
import networkx as nx
import re
import csv
from datetime import datetime

# indicate the input and output folder
# YYYYMM = datetime.now().strftime("%Y%m")
YYYYMM = '201607'
inputdir = 'Input_' + YYYYMM + '/'
rawdir = 'Rawdata_' + YYYYMM + '/'
outputdir = 'Output_' + YYYYMM + '/'

def find_delivery_date(htmlfile):
	soup = BeautifulSoup(htmlfile, 'html.parser')
	tag = soup.find(class_="birth")
	print str(tag)
	#delivery_date = re.search(r'<span class="birth">(.*) 出生</span>', str(tag), re.M|re.I)
	#delivery_date_list = re.findall(r'\d+', str(tag))
	delivery_date_list = re.findall(r'\d+', str(tag))
	output = '-'.join(delivery_date_list)
	print "delivery_date: ", output
	return output

def haha():
	with open(inputdir + 'babytree_user_id_random10.csv', 'rU') as csvfile:
		user_id_list = csv.reader(csvfile, delimiter = ',')
		for user_id_row in user_id_list:
			try:
				filename = user_id_row[0]
				f = open(rawdir + filename,'r')
				delivery_date = find_delivery_date(f)
				f.close()
				f2 = open(outputdir + 'User_delivery_date.txt','a')
				print user_id_row[0] + '\'s delivery date is: ' + delivery_date
				f2.write(user_id_row[0] + ';' + delivery_date + '\n')
				f2.close()
				# break
			except:
				print user_id_row[0] + ' not found'
				continue

if __name__ = "__main__":
	haha()

# def post_number
# count = 1


# 'http://home.babytree.com/u128475590597/info/mytopic/?Ttype=post&pg=' + count
# count += 1


