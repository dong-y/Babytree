from bs4 import BeautifulSoup
import pprint
import mechanize
import re
import os
from urllib2 import HTTPError

browser = mechanize.Browser()

for content_file in os.listdir('/Users/dong/Downloads'):
	if content_file.startswith('content_page'):
		print "content_file = ", content_file
		content_file_number = re.findall(r'\d+', content_file)[0]
		path_content_file = '/Users/dong/Downloads/' + content_file
		html_file = open(path_content_file, 'r')
		html_file_page_content = html_file.read()
		soup = BeautifulSoup(html_file_page_content)
		table_tag = soup.find('table')
		link_list = []
		count = 1
		for td_tag in table_tag.findAll("td", { "class" : "topicTitle" }):
			a_tag = td_tag.find('a')
			a_tag_list = td_tag.findAll('a')
			a_tag_last_page = a_tag_list[len(a_tag_list) - 1]
			last_page_number = None
			if len(a_tag_list) == 1:
				last_page_number = 1
			else:
				last_page_file_number_index_list = re.findall(r'\d+', a_tag_last_page['href'])
				last_page_number = int(last_page_file_number_index_list[len(last_page_file_number_index_list) - 1])
				print a_tag_last_page, last_page_number
			link_list.append(a_tag['href'])
			a_tag_first_page_link = a_tag_list[0]['href']
			a_tag_first_page_link_first_part = a_tag_first_page_link.split('.')[0]
			for page in range(1, last_page_number + 1):
				page_url = None
				if last_page_number == 1:
					page_url = a_tag['href']
				else:
					page_url = a_tag['href'].split('.')[0] + '.' + a_tag['href'].split('.')[1] + '.' + a_tag['href'].split('.')[2] + '_' + str(page) + '.html'
				print 'page_url = ', page_url
				# newpath_directory = '/Users/dong/Downloads/' + 'link_' + content_file_number + '_' + str(count) + '/'
				newpath_directory = a_tag['href'].split('.')[0] + '.' + a_tag['href'].split('.')[1] + '.' + a_tag['href'].split('.')[2]
				newpath_directory = newpath_directory.replace('/', '_')
				newpath_directory = '/Users/dong/Downloads/' + newpath_directory + '/'
				if not os.path.exists(newpath_directory):
					os.makedirs(newpath_directory)
				# file_stream = open(newpath_directory + 'page_' + str(page) + '.txt', 'w')				
				page_url_new = page_url.replace('/', '_')
				if not os.path.isfile(newpath_directory + page_url_new + '.txt'):
					print 'Angel is awesome'
					try:
						response = browser.open(page_url)
						print "Shubham is stupid"
						page_content = response.read()
						print newpath_directory + page_url_new + '.txt'
						file_stream = open(newpath_directory + page_url_new + '.txt', 'w')
						file_stream.write(page_content)
						file_stream.close()
					except HTTPError:
						print "Angel is soooooooo awesome"
						continue
					except urllib2.URLError:
						print "Shubham is OK"
						page = page - 1
    					continue
					
					
			count = count + 1
		# pprint.pprint(link_list)
		# count = 1
		# for link in link_list:
		# 	try:
		# 		response = browser.open(link)
		# 	except HTTPError, e:
		# 		print "Got error code ", e.code
		# 		continue
		# 	response_text = response.read()
		# 	newpath_directory = '/Users/dong/Downloads/' + 'link_' + content_file_number + '_' + str(count) + '/'
		# 	if not os.path.exists(newpath_directory):
		# 		os.makedirs(newpath_directory)

			# content_file_name = 'link_' + content_file_number + '_' + str(count) + '.txt'
			# content_file_stream = open(content_file_name, 'w')
			# content_file_stream.write(response_text)
			# content_file_stream.close()
		html_file.close()