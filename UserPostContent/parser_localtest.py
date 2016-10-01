# -*- coding: utf-8 -*-
import os
from bs4 import BeautifulSoup
import codecs
import re


def find_id(div_post):
	user_name_text = div_post.find('p',class_ = 'userName').a
	url = user_name_text.get('href')
	userid = url[25:]
	# print(user_name_text.string)
	return userid

def find_forum_level_from_li_from_post_div(div_post):
	list_from_post = div_post.find(class_ = 'userProfileDetail')
	p = re.compile(r'等级：(.*)</li><li>')  #<li>等级：铜牌</li>
	# print('list_from_post = ', list_from_post)
	forum_level = re.search(p, str(list_from_post)).group(1)[0:2]
	# print('forum_level = ', forum_level)
	return forum_level

def find_city_from_li_from_post_div(div_post):
	try:
		list_from_post = div_post.find('ul', {'class': 'userProfileDetail'})
		p = re.compile(r'来自：<a target="_blank" rel="nofollow" href="http://(.*).city.babytree.com/">')
		city = re.search(p, str(list_from_post)).group(1)
		return city
	except AttributeError:
		return "NULL"

def find_hospital_from_li_from_post_div(div_post):
	try:
		list_from_post = div_post.find(class_ ='userProfileDetail')
		p = re.compile(r'#E00;">(.*)</a></li>')
		hospital = re.search(p, str(list_from_post)).group(1)
		# print(list_from_post)
		q = re.compile(r'hospital(.*)/\"')
		hospital_no = re.search(q, str(list_from_post)).group(1)
		return hospital, hospital_no
	except AttributeError:
		return "NULL"

def find_timestamp_from_post_div(div_post):
	try:
		timestamp_str = div_post.find('div', {'class': 'postBody'}).find('p', {'class': 'postTime'})
		# print(timestamp_str)
		p = re.compile(r'\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d')
		# print(re.search(p, str(timestamp_str)))
		timestamp = re.search(p, str(timestamp_str)).group(0)
		# print(timestamp)	
		return timestamp
	except AttributeError:
		return "NULL"

def find_post_content(soup):
	print("******* POST CONTENT *******")
	if soup.find(id = "Vote"):
		topicContent = soup.find('babytreevote')
	else:
		topicContent = clubTopicSinglePost.find(id = 'topic_content')
	content = topicContent.get_text()
	content = content.replace("document.write('回复')回复\n\ndocument.write('举报')举报\n\n", '')
	content = content.replace('\n', '') #bleach the text a bit
	imagecnt = len(topicContent.find_all('img'))
	print("Content = ", content)
	print("Image count = ", imagecnt)
	print("***************************")
	return imagecnt, content

def find_user_info(div_post):
	print("******** USER INFO ********")
	user_info = []
	# username = find_user_from_post_div(div_post)[0]
	# print("username = ", username)
	userid = find_id(div_post)
	timestamp = find_timestamp_from_post_div(div_post)
	forum_level = find_forum_level_from_li_from_post_div(div_post)
	city = find_city_from_li_from_post_div(div_post)
	hospital = find_hospital_from_li_from_post_div(div_post)[0]
	hospital_no = find_hospital_from_li_from_post_div(div_post)[1]
	user_info = [userid, timestamp, forum_level, city, hospital, hospital_no]
	print("userid = ", userid)
	print("timestamp = ", timestamp)
	print("forum_level = ", forum_level)
	print("city = ", city)
	print("hospital = ", hospital)
	print("hospital number = ", hospital_no)
	print("**************************")
	return user_info

def main():
	with codecs.open('demo.html', "r", encoding='utf-8', errors='ignore') as fdata:
		soup = BeautifulSoup(fdata)
		clubTopicSinglePost = soup.find('div', {'class': 'clubTopicSinglePost'})
		user_info = find_user_info(clubTopicSinglePost)
		something = find_post_content(soup)
		content = something[1]
		imagecnt = something[0]
		# user_info.append(str(imagecnt))
		user_info.append(str(something[0]))
		user_info.append(something[1])
		print(user_info)
		outputtext = '\t'.join(user_info)
		print(outputtext)
	outf = 'babytree_user_post_content.csv'
	f = codecs.open(outf,'a', 'utf-8')
	f.write(outputtext + '\n')
	f.close()

main()
