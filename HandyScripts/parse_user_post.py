# -*- coding: utf-8 -*-
import os
# from natsort import natsorted
from bs4 import BeautifulSoup
import codecs
# import networkx as nx
import re
import csv
import codecs

# loop different pages from 1, 2, 3, ...
# loop all the files
# parse user_id, post_title, board, date
# then use jieba to seperate the titles

def find_title(htmltag):
	title = htmltag.find('a').get('title')
	print 'title = ', title
	return title

def find_board(htmltag):
	piece_for_board = htmltag.find('a', class_='board')
	board = re.search(r'community\/(.*)\/\" target', str(piece_for_board), re.M|re.I)
	board = str(board.group(1))
	print 'board = ', board 
	return board

def find_date(htmltag):
	piece_for_date = htmltag.find(nowrap="nowrap").find('span', class_='ls')
	# print piece_for_date
	date = piece_for_date.contents[0]
	date = date.replace(' ','')	
	date = date.replace('-','')	
	date = date.replace('\n', '')
	date = date[:8]
	print 'date = ', date
	return date

with open('postpartum_depression_user_id.csv', 'rU') as csvfile:
	user_id_list = csv.reader(csvfile, delimiter = ';')
	for user_id_row in user_id_list:
		count = 1
		while True:
			filename = user_id_row[0] + "_post_" + str(count)
			print filename
			if os.path.isfile(filename):
				f = open(filename,'r')
				soup = BeautifulSoup(f, 'html.parser')
				posts_string = soup.find(id="TbBbs")
				posts_list = posts_string.find_all('tr')
				# print posts_list
				for post in posts_list:
					try:
						title = find_title(post)
						if title == None:
							title = "private"
						board = find_board(post)
						date = find_date(post)
						f2 = codecs.open('babytree_user_post.csv','a', 'utf-8')
						f2.write(user_id_row[0] + ';post;' + str(count) + ';'  + board + ';' + date + ';' + title + ';\n')
						f2.close()
						# f3 = codecs.open('babytree_user_post_only.txt', 'a', 'utf-8')
						# f3.write(title + '\n')
						# f3.close()
					except AttributeError:
						f4 = open('parser_AttributeError.txt', 'a')
						f4.write(filename)
						f4.close()
						pass
				f.close()
			else:
				break
			count += 1
		

