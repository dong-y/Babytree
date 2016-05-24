# -*- coding: utf-8 -*-
#merge two csv files based on user_id
import csv
import pandas as pd
# from collections import OrderedDict

# with open('b.csv', 'rb') as f:
#     r = csv.reader(f)
#     dict2 = {row[0]: row[1:] for row in r}

# with open('a.csv', 'rb') as f:
#     r = csv.reader(f)
#     dict1 = OrderedDict((row[0], row[1:]) for row in r)

# result = OrderedDict()
# for d in (dict1, dict2):
#     for key, value in d.iteritems():
#         result.setdefault(key, []).extend(value)

# with open('ab_combined.csv', 'wb') as f:
#     w = csv.writer(f)
#     for key, value in result.iteritems():
#         w.writerow([key] + value)

# with open('babytree_user_post_onlyurl.csv', 'rU') as csvfile1:
# 	data1 = csv.reader(csvfile1, delimiter = ';')
# 	with open('babytree_user_delivery_date.csv', 'rU') as csvfile2:
# 		data2 = csv.reader(csvfile2, delimiter = ';')
# 		for row in reader:
# 			user_id	= row[0]
# 			post = row[1]
# 			board = row[2]
# 			date = row[3]
# 			url = row[4]


a = pd.read_csv("a.csv")
b = pd.read_csv("b.csv")
# b = b.dropna(axis=1)
merged = a.merge(b, on="name")
merged.to_csv("ab.csv", index=False)




