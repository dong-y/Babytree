# -*- coding: utf-8 -*-
import os
from bs4 import BeautifulSoup
import codecs
import re
import csv
import codecs

with open('babytree_user_post_url.csv', 'rU') as csvfile:
	rows = csv.reader(csvfile, delimiter = ';')
	for row in rows:
		user_id = row[0]
		# print user_id
		if user_id[0] != 'u': 
			print user_id
			print rows.line_num
	print "Done!"

