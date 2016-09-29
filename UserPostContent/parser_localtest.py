# -*- coding: utf-8 -*-
import os
from bs4 import BeautifulSoup

f = open('demo.html', 'r')
webpage = BeautifulSoup(f, 'html.parser')
title = webpage.title.string
print(title)