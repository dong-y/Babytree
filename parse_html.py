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
	user_name_tag = div_post.find('div', {'class': 'postUserProfile'}).find('p', {'class': 'userName'}).find('a')
	if not user_name_tag:
		user_name_tag = div_post.find('div', {'class': 'postUserProfile'}).find('p', {'class': 'userName'})
	p = re.compile(r'(\')(.*)(\')')
	# print(user_name_tag.contents[1])
	nick_name = re.search(p, str(user_name_tag.contents[1])).group(2)
	# user_name = user_name_tag['href']
	# return user_name.rsplit('/', 1)[1]
	return nick_name

def tell_id_from_nickname(div_post):
	try:
		id_tag = div_post.find('div', {'class': 'postUserProfile'}).find('p', {'class': 'userName'})
		p = re.compile(r'http://home.babytree.com/(.*)\"')
		id = re.search(p, str(id_tag.contents[1]))
		print(id)
		return id
	except AttributeError:
		return 

def find_reply_to_user_from_post_div(div_post):
	span_tag = div_post.find('span', {'name': 'babytree_refer'})
	p = re.compile(r'回复  (.*)  \d')
	# print(span_tag.contents[0])
	# print(re.search(p, str(span_tag)).group(1))
	return re.search(p, str(span_tag)).group(1)

def find_list_from_post_div(div_post):
	li = div_post.find('ul', {'class': 'userProfileDetail'}).find_all('li')
	return li

# def find_userProfileDetial_from_li(li):


def find_timestamp_from_post_div(div_post):
	try:
		timestamp_str = div_post.find('div', {'class': 'postBody'}).find('p', {'class': 'postTime'})
		# print(timestamp_str)
		p = re.compile(r'\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d')
		# print(re.search(p, str(timestamp_str)))
		timestamp = (re.search(p, str(timestamp_str))).group(0)
		# print(timestamp)	
		return timestamp
	except AttributeError:
		return 
	

def find_responsenumber_from_post_div(div_post):
	try:
		responsenumber =  div_post.find('div',{'class': ''}).find('p',{'class': ''})
		return responsenumber
		
	except AttributeError:
		return 

def find_floornumber_from_post_div(div_post):




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
					try:
						post_user = find_user_from_post_div(div_post)
					except IndexError:
						break
					except AttributeError:
						break
					# G.add_node(post_user)
					timestamp_post = find_timestamp_from_post_div(div_post)
					if is_some_user_referred_in_reply(div_post):
						reply_to_user = find_reply_to_user_from_post_div(div_post)
						# if not (post_user == reply_to_user):
						# 	if not G.has_edge(post_user, reply_to_user):
						# 		G.add_edge(post_user, reply_to_user, weight=1)
							# else:
							# 	G[post_user][reply_to_user]['weight'] += 1
						with open('babytree_database.csv', 'a', newline='') as csvfile:
							spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
							spamwriter.writerow([post_user, reply_to_user, timestamp_post])
					if is_some_user_quoted_in_reply(div_post):
						quoted_user = find_quoted_user_from_post_div(div_post)
						with open('babytree_database.csv', 'a', newline='') as csvfile:
							spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
							spamwriter.writerow([post_user, quoted_user, timestamp_post])
						# if not (post_user == quoted_user):
						# 	if not G.has_edge(post_user, quoted_user):
						# 		G.add_edge(post_user, quoted_user, weight=1)
						# 	else:
						# 		G[post_user][quoted_user]['weight'] += 1
					if (j == 0) and (i == 0):
						# print("I am here!")
						first_user = post_user
						with open('babytree_database.csv', 'a', newline='') as csvfile:
							spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
							spamwriter.writerow([post_user, '', timestamp_post])
					elif post_user == first_user:
						with open('babytree_database.csv', 'a', newline='') as csvfile:
							spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
							spamwriter.writerow([post_user, post_user, timestamp_post])
						continue						
					else:
						# if not G.has_edge(post_user, first_user):
						# 	G.add_edge(post_user, first_user, weight=1)
						# else:
						# 	G[post_user][first_user]['weight'] += 1
						with open('babytree_database.csv', 'a', newline='') as csvfile:
							spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
							spamwriter.writerow([post_user, first_user, timestamp_post])
					# print(G.nodes())
					# print(G.edges())
				# nx.write_gml(G,"path.to.file")
				# nx.draw(G)
				# plt.show()
				# input("Enter to continue")