# -*- coding: utf-8 -*-
import os
from bs4 import BeautifulSoup
import codecs
import re
import csv
import urllib2
from datetime import datetime
import sys

reload(sys)  # is it really useful?
sys.setdefaultencoding('utf8')

def find_id(div_post):
	user_name_text = div_post.find(class_ = 'userName').a
	url = user_name_text.get('href')
	userid = url[25:]
	# print(user_name_text.string)
	return userid

def find_forum_level(div_post):
	list_from_post = div_post.find(class_ = 'userProfileDetail')
	# print list_from_post
	p = re.compile(r'等级：(.*?)</li><li>')  #<li>等级：铜牌</li>
	# print('list_from_post = ', list_from_post)
	forum_level = re.search(p, str(list_from_post)).group(1)
	# print('forum_level = ', forum_level)
	# print forum_level
	try:
		dict = {'普通': '0', '铁牌': '1', '铜牌': '2', '银牌': '3', '金牌': '4'}
		forum_level = dict[forum_level]
	except:
		forum_level = 'null'
	return forum_level

def find_city(div_post):
	list_from_post = div_post.find(class_ = 'userProfileDetail')
	# print 'I\'m here'
	# print list_from_post
	p = re.compile(r'来自：<a target=\"_blank\" rel=\"nofollow\" href=\"http://(.*).babytree.com/')
	city = re.search(p, str(list_from_post)).group(1)
	city = city.replace('.city','')
	return city

def find_hospital(div_post):
	list_from_post = div_post.find(class_ ='userProfileDetail')
	try:
		p = re.compile(r'#E00;\">(.*)</a></li>')
		hospital = re.search(p, str(list_from_post)).group(1)
		# print(list_from_post)
		q = re.compile(r'hospital(.*)/\"')
		hospital_no = re.search(q, str(list_from_post)).group(1)
	except:
		hospital = 'null'
		hospital_no = 'null'
	return hospital, hospital_no

def find_datetime(div_post):
	try:
		timestamp_str = div_post.find('div', {'class': 'postBody'}).find('p', {'class': 'postTime'})
		# print(timestamp_str)
		p = re.compile(r'\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d')
		# print(re.search(p, str(timestamp_str)))
		timestamp = re.search(p, str(timestamp_str)).group(0)
		# print(timestamp)	
		return timestamp
	except AttributeError:
		return 'NULL'

def find_post_content(soup):
	# print('******* POST CONTENT *******')
	print '******* POST CONTENT *******'
	if soup.find(id = 'Vote'):
		topicContent = soup.find('babytreevote')
		content = content.replace('document.write(\'回复\')回复\n\ndocument.write(\'举报\')举报\n\n', '')
	else:
		clubTopicSinglePost = soup.find(class_ = 'clubTopicSinglePost')
		topicContent = clubTopicSinglePost.find(id = 'topic_content')
	content = topicContent.get_text()
	# print content
	chars_to_remove = ['\n', '\t', ' ', '该帖子已经被发帖用户删除']
	imagecnt = len(topicContent.find_all('img'))
	for char in chars_to_remove:
		content = content.replace(char, '')
	# content.translate(None, ''.join(chars_to_remove)) #bleach the text a bit
	print 'Content = ', content
	print 'Image count = ', imagecnt
	print '***************************'
	# print('Content = ', content)
	# print('Image count = ', imagecnt)
	# print('***************************')
	return imagecnt, content

def find_user_info(div_post):
	# print('******** USER INFO ********')
	print '********* USER INFO *********'
	user_info = []
	# username = find_user_from_post_div(div_post)[0]
	# print('username = ', username)
	userid = find_id(div_post)
	timestamp = find_datetime(div_post)
	forum_level = find_forum_level(div_post)
	city = find_city(div_post)
	hospital = find_hospital(div_post)[0]
	hospital_no = find_hospital(div_post)[1]
	# user_info = [userid, timestamp, forum_level, city, hospital, hospital_no]
	user_info = [userid, forum_level, timestamp, city, hospital_no]
	# print('userid = ', userid)
	# print('timestamp = ', timestamp)
	# print('forum_level = ', forum_level)
	# print('city = ', city)
	# print('hospital = ', hospital)
	# print('hospital number = ', hospital_no)
	# print('**************************')
	print 'userid = ', userid
	print 'timestamp = ', timestamp
	print 'forum_level = ', forum_level
	print 'city = ', city
	print 'hospital = ', hospital
	print 'hospital number = ', hospital_no
	print '****************************'
	return user_info

def get_n_write_info(url, inputf, outf, outf2):
	try:
		with codecs.open(inputf, 'r', encoding='utf-8', errors='ignore') as fdata:
			soup = BeautifulSoup(fdata)
			# print soup
			clubTopicSinglePost = soup.find(class_ = 'clubTopicSinglePost')
			# print clubTopicSinglePost
			info_eng = find_user_info(clubTopicSinglePost)
			something = find_post_content(soup)
			content_cn = something[1]
			imagecnt = something[0] #is there easier way to turn tuple into list?
			title = soup.title.string
			info_eng.append(str(imagecnt))
			# user_info.append(something[1])
			# user_info.append(title)
			# print(user_info)
			info_eng = '\t'.join(info_eng)
			# print(outputtext)
	except: 
		info_eng = ''
		content_cn = ''
	f = codecs.open(outf,'a', 'utf-8')
	print info_eng
	f.write(url + '\t' + info_eng + '\n') #exclude the Chinese content
	f.close()
	f2 = codecs.open(outf2, 'a', 'utf-8')
	print content_cn
	f2.write(url + '\t' + content_cn + '\n')
	f2.close()

def main():
	# output variables
	variables = ['url','user_id', 'forum_level', 'timestamp', 'city', 'hospital_no', 'imagecnt']
	# initialization (this is ugly - fix it later)
	YYYYMM = '201607'
	inputdir = 'Input_' + YYYYMM + '/'
	rawdir = 'Rawdata_' + YYYYMM + '/'
	outputdir = 'Output_' + YYYYMM + '/'
	outf = outputdir + 'babytree_user_post_content.csv'
	outf2 = outputdir + 'babytree_user_post_content_text.csv'
	errorf = outputdir + 'ioerror_parsing.txt'
	outfs = [outf, outf2, errorf]
	for f in outfs:
		if os.path.exists(f):
			os.remove(f)
	f = open(outf,'w') 
	f.write('\t'.join(variables) + '\n')
	f.close()
	count = 1
	with open(inputdir + 'babytree_user_post_url.csv', 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter = ';')
		for row in reader:
			# if count <10:	#pretest
			print '**********************************************************'
			print '*********** Do not worry, I am parsing No.%d file ********' %(count)
			user_id = row[0]
			url = row[4]
			url_filename = url.replace('/','_').replace(':','_').replace('.','_')
			inputf = rawdir + url_filename
			# print inputf #############
			if os.path.isfile(inputf):
				print '****** Hi! File exists ******'
				get_n_write_info(url, inputf, outf, outf2)
			else:
				print url + ' file does not exist'
				f = open('ioerror_parsing.txt','a')
				f.write(url + '\n')
				f.close()
			count += 1
			print '**********************************************************'
			# break #let's pretest it once

main()

