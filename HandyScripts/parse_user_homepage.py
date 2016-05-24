import os
from natsort import natsorted
from bs4 import BeautifulSoup
import codecs
import networkx as nx
import re
import csv


def find_delivery_date(htmlfile):
	soup = BeautifulSoup(htmlfile, 'html.parser')
	tag = soup.find_all(id="mytree-basic-info")
	# print str(tag)
	delivery_date = re.search(r'<span class="none" data="(.*)">', str(tag), re.M|re.I)
	print "delivery_date: ", delivery_date.group(1)
	return delivery_date
	
	
with open('babytree_user_id.csv', 'rU') as csvfile:
	user_id_list = csv.reader(csvfile, delimiter = ';')
	for user_id_row in user_id_list:
		filename = user_id_row[0]
		f = open(filename,'r')
		delivery_date = find_delivery_date(f)
		f.close()
		f2 = open('user_delivery_date','a')
		f2.write(filename + ';' + delivery_date + '\n')
		f2.close()
		

