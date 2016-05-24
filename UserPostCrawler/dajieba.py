# encoding=utf-8
import os
from natsort import natsorted
from bs4 import BeautifulSoup
import codecs
import networkx as nx
import re
import csv
import codecs
import jieba

# with open('babytree_user_post') as f:
#       posts = f.readlines()
#       for post in posts:
#             seg_list = jieba.cut('为什么这个程序叫结巴',cut_all=True)
#             print ", ".join(seg_list)

with open('babytree_user_post.csv') as csvfile:
      rows = csv.reader(csvfile, delimiter = ';')
      for row in rows:
            post_title = row[2]
            print post_title
            post_seg = jieba.cut(post_title, cut_all=False)
            print ', '.join(post_seg)
            # f2 = codecs.open('babytree_user_post_jieba.csv','a', 'utf-8')
            # f2.write(row + ';' + post_seg + ';\n')
            # f2.close()

