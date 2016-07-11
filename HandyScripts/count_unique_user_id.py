# encoding=utf-8
import os
import re
import csv
import codecs


with open('babytree_user_post.csv') as csvfile:
	rows = csv.reader(csvfile, delimiter = ';')
	# user_id_list = []
	# for row in rows:
	# 	user_id_list.append(str(row[0]))
	# unique_value = len(set(user_id_list))
	# i = 1
	# count = 1
	# for user in user_id_list:
	# 	# print user_id_list[1]
	# 	try:
	# 		if user_id_list[i] != user_id_list[i-1]:
	# 			count += 1
	# 		i += 1
	# 	except IndexError:
	# 		break
	# print count


	# cur = user_id_list[0]
	# count = 1
	# for user in user_id_list:
	# 	if cur!=user:
	# 		count+=1
	# 		cur = user
	# # print unique_value
	# print count

	count = 0
	current	 = ''
	# print rows
	for row in rows:
		print row
		row = str(row[0]) 
		# print row
		if current != row:
			count += 1 
			current = row 
	print count 

# list = [1,2,3]
# list_2 = [2,3]
# list_of_list = [list, list_2]
# print list_of_list