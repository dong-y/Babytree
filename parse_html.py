import os
from natsort import natsorted
from bs4 import BeautifulSoup
import codecs
import networkx as nx
import matplotlib.pyplot as plt
import re
import csv

rootdir = '/Users/dong/Downloads/20150213/'
# G = nx.DiGraph()
# print(G)

def find_user_from_post_div(div_post):
	try:
		user_name_tag = div_post.find('div', {'class': 'postUserProfile'}).find('p', {'class': 'userName'}).find('a')
		if not user_name_tag:
			user_name_tag = div_post.find('div', {'class': 'postUserProfile'}).find('p', {'class': 'userName'})
		p = re.compile(r'(\')(.*)(\')') 
		# print(user_name_tag.contents[1])
		nick_name = re.search(p, str(user_name_tag.contents[1])).group(2)
		# user_name = user_name_tag['href']
		# return user_name.rsplit('/', 1)[1]
		return nick_name
	except IndexError:
		return "NULL"
	except AttributeError:
		return "NULL"

def tell_id_from_nickname(div_post):
	try:
		id_tag = div_post.find('div', {'class': 'postUserProfile'}).find('p', {'class': 'userName'})
		p = re.compile(r'href="http://home.babytree.com/(.*)" target="_blank">')
		# print("id_tag.contents = ", id_tag.contents)
		id = re.search(p, str(id_tag.contents[1])).group(1)
		# print("id = ", id)
		return id
	except IndexError:
		return "NULL"
	except AttributeError:
		return "NULL"

def find_forum_level_from_li_from_post_div(div_post):
	try:
		list_from_post = div_post.find('ul', {'class': 'userProfileDetail'})
		p = re.compile(r'等级：(.*)级')
		print('list_from_post = ', list_from_post)
		forum_level = re.search(p, str(list_from_post)).group(1)
		# print('forum_level = ', forum_level)
		return forum_level
	except AttributeError:
		return "NULL"

def find_preg_status_from_li_from_post_div(div_post):
	try:
		list_from_post = div_post.find('ul', {'class': 'userProfileDetail'})
		print("ul_element = ", list_from_post)
		script_elements = div_post.find_all('script')
		print("script_elements = ", script_elements)
	except AttributeError:
		return "NULL"
		# li_elements = list_from_post.find('li')
		# print("li_elements = ", )
		# p = re.compile(r'<li>(.*)<a target="_blank"  href="http://www.babytree.com/community/club(.*)/">孕')
		# preg_status = re.search(p, str(list_from_post)).group(1) + re.search(p, str(list_from_post)).group(2)
		# print("preg_status_re_group_1 = ", re.search(p, str(list_from_post)).group(1))
		# print("preg_status_re_group_2 = ", re.search(p, str(list_from_post)).group(2))
		# return preg_status

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
		list_from_post = div_post.find('ul', {'class': 'userProfileDetail'})
		p = re.compile(r'#E00;">(.*)</a></li>')
		hospital = re.search(p, str(list_from_post)).group(1)
		return hospital
	except AttributeError:
		return

def find_response_number_from_post_div(div_post):
	# try:
		# print("div_post = ", div_post)
		# response_number_tag =  div_post.find('div',{'class': 'clubTopicList'})
		# p = re.compile(r'div id="response_(.*)" ')
		# print('response_number_tag = ', response_number_tag)
		# response_number = re.search(p, str(response_number_tag))
		# return response_number
	print(div_post.attrs)
	if 'id' in div_post.attrs:
		p = re.compile(r'response_(.*)')
		return re.search(p, div_post["id"]).group(1)
	# except AttributeError:
	# 	return 

def find_floor_number_from_post_div(div_post):
	# try:
		floor_div = div_post.find('div',{'class':'postUserProfile'})
		if 'id' in floor_div.attrs:
			p = re.compile(r'floor_(.*)')
			return re.search(p, floor_div['id']).group(1)
		# p = re.compile(r'div id="floor_(.*)" ')
		# floor_number = re.search(p, str(floor_number))
		
	# except AttributeError:
	# 	return

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

def find_reply_to_user_from_post_div(div_post):
	span_tag = div_post.find('span', {'name': 'babytree_refer'})
	p = re.compile(r'回复 &nbsp;(.*)&nbsp;')
	# print(span_tag.contents[0])
	# print(re.search(p, str(span_tag)).group(1))
	return re.search(p, str(span_tag))

def is_some_user_referred_in_reply(div_post):
	span_tag = div_post.find('span', {'name': 'babytree_refer'})
	if not span_tag:
		return span_tag
	else:
		p = re.compile(r'回复  (.*)  \d')
		return re.search(p, str(span_tag))

def is_some_user_quoted_in_reply(div_post):
	span_tag = div_post.find('span', {'name': 'babytree_refer'})
	if not span_tag:
		return span_tag
	else:
		p = re.compile(r'&nbsp;(.*)回复道')
		return re.search(p, str(span_tag))

def find_quoted_user_from_post_div(div_post):
	span_tag = div_post.find('span', {'name': 'babytree_refer'})
	p = re.compile(r'&nbsp;(.*)回复道')
	return re.search(p, str(span_tag)).group(1)


for subdir, dirs, files in os.walk(rootdir):
	if subdir.startswith('/Users/dong/Downloads/20150213/http'):
		p = re.compile(r'http://www.babytree.com/community/(.*)')
		topic_id = re.search(p, str(subdir))
		file_list = natsorted(files)
		# print(subdir)
		first_user = None
		for i in range(0, len(file_list)):
			file_name = file_list[i]
			file_path = subdir + '/' + file_name
			print(file_path)
			# file = open(file_path)
			with codecs.open(file_path, "r", encoding='utf-8', errors='ignore') as fdata:
				soup = BeautifulSoup(fdata)
				div_posts = soup.find_all('div', {'class': 'clubTopicSinglePost'})
				for j in range(0, len(div_posts)):
					div_post = div_posts[j]
					# try:
					post_user = find_user_from_post_div(div_post)
					print("post_user = ", post_user)
					post_user_id = tell_id_from_nickname(div_post)
					print("post_user_id", post_user_id)
					timestamp_post = find_timestamp_from_post_div(div_post)
					print("timestamp_post = ", timestamp_post)
					response_number = find_response_number_from_post_div(div_post)
					print("response_number = ", response_number)
					floor_number = find_floor_number_from_post_div(div_post)
					print("floor_number = ", floor_number)
					preg_status = find_preg_status_from_li_from_post_div(div_post)
					print("preg_status = ", preg_status)
					forum_level = find_forum_level_from_li_from_post_div(div_post)
					print("forum_level = ", forum_level)
					city = find_city_from_li_from_post_div(div_post)
					print("city = ", city)
					hospital = find_hospital_from_li_from_post_div(div_post)
					print("hospital = ", hospital)
					with open('babytree_database_2.csv', 'a', newline='') as csvfile:
						spamwriter = csv.writer(csvfile, delimiter=';',quotechar=' ', quoting=csv.QUOTE_MINIMAL)
						print([post_user, post_user_id, timestamp_post, floor_number, preg_status, forum_level, city, hospital ])
						spamwriter.writerow([post_user, post_user_id, timestamp_post, response_number, preg_status, floor_number, forum_level, city, hospital ])
					# input("Press Enter to continue...")	
					# except IndexError:
					# 	print("IndexError")
					# 	break
					# except AttributeError:
					# 	print("AttributeError")
					# 	break
					# G.add_node(post_user)
					
					# if is_some_user_referred_in_reply(div_post):
					# 	reply_to_user = find_reply_to_user_from_post_div(div_post)
					# 	# if not (post_user == reply_to_user):
					# 	# 	if not G.has_edge(post_user, reply_to_user):
					# 	# 		G.add_edge(post_user, reply_to_user, weight=1)
					# 		# else:
					# 		# 	G[post_user][reply_to_user]['weight'] += 1
					# 	with open('babytree_database.csv', 'a', newline='') as csvfile:
					# 		spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
					# 		spamwriter.writerow([post_user, reply_to_user, timestamp_post])
					# if is_some_user_quoted_in_reply(div_post):
					# 	quoted_user = find_quoted_user_from_post_div(div_post)
					# 	with open('babytree_database.csv', 'a', newline='') as csvfile:
					# 		spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
					# 		spamwriter.writerow([post_user, quoted_user, timestamp_post])
					# 	if not (post_user == quoted_user):
					# 		if not G.has_edge(post_user, quoted_user):
					# 			G.add_edge(post_user, quoted_user, weight=1)
					# 		else:
					# 			G[post_user][quoted_user]['weight'] += 1
					# if (j == 0) and (i == 0):
					# 	# print("I am here!")
					# 	first_user = post_user
					# 	with open('babytree_database.csv', 'a', newline='') as csvfile:
					# 		spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
					# 		spamwriter.writerow([post_user, '', timestamp_post])
					# elif post_user == first_user:
					# 	with open('babytree_database.csv', 'a', newline='') as csvfile:
					# 		spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
					# 		spamwriter.writerow([post_user, post_user, timestamp_post])
					# 	continue						
					# else:
					# 	# if not G.has_edge(post_user, first_user):
					# 	# 	G.add_edge(post_user, first_user, weight=1)
					# 	# else:
					# 	# 	G[post_user][first_user]['weight'] += 1
					# 	with open('babytree_database.csv', 'a', newline='') as csvfile:
					# 		spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
					# 		spamwriter.writerow([post_user, first_user, timestamp_post])
					# print(G.nodes())
					# print(G.edges())
				# nx.write_gml(G,"path.to.file")
				# nx.draw(G)
				# plt.show()
				# input("Enter to continue")