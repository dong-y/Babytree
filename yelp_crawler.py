from bs4 import BeautifulSoup
import requests
import sys
import mechanize
import pprint

browser = mechanize.Browser()
# browser.set_handle_robots(False)

# bars = {}

# bars_list = []
for i in range(86, 501):
	print i
	response = None
	url = ''
	if i == 0:
		url = 'http://www.babytree.com/community/birthclub/preg_1_1.html'
	else:
		# url = 'http://www.yelp.com.sg/search?find_desc=Sports+Bar&find_loc=Singapore&ns=1#start='+str(i*10)
		url = 'http://www.babytree.com/community/birthclub/preg_1_' + str(i+1) + '.html'
	response = browser.open(url)
	file_name = "content_page_" + str(i + 1) + ".txt"
	file_stream = open(file_name, 'w')
	html_doc = response.read()
	file_stream.write(html_doc)
	file_stream.close()
	pprint.pprint(html_doc)
	# soup = BeautifulSoup(html_doc)
	# new_bars_list = soup.find_all("div", class_="search-result natural-search-result biz-listing-large")
	# # pprint.pprint(new_bars_list)
	# for new_bar in new_bars_list:
	# 	bar_name = new_bar.find('a', class_="biz-name").string
	# 	bars[bar_name] = {}
	# pprint.pprint(bars)
	# bars_list = bars_list + new_bars_list
	
# pprint.pprint(bars_list)

# CONSUMER_KEY = 'Dg60F7zpCwjEe0-6zKCF_Q'
# CONSUMER_SECRET = 'QNF6yVM2yEAxr0vHWsLorswCgio'
# TOKEN = '8cX-4eg7Q4oJIdECnDOI_qfpkCTNVl4I'
# TOKEN_SECRET = '4zhXE_Ue6ncEGwgYQ8qrjrFRY3o'