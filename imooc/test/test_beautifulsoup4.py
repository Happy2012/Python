#!/usr/bin/env python        
# -*- coding: utf-8 -*-
"""
__title__ =  'test_beautifulsoup4.py'
__author__ = 'Amanda'
__mtime__ = '2018-12-24 16:08'
__summary__ = '网页解析-beautifulsoup第三方插件的使用'
"""
import re
from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
#soup = BeautifulSoup(html_doc, 'html.parser',from_encoding='utf-8')
soup = BeautifulSoup(html_doc, 'html.parser')
print('获取所有的链接')
links = soup.find_all('a')
for link_node in links:
	print(link_node.name, link_node['href'], link_node.get_text())
print('获取Lacie的链接')
link_node = soup.find( 'a', href ='http://example.com/lacie')
print(link_node.name, link_node['href'], link_node.get_text())
print('正则表达式匹配')
link_node = soup.find('a',href = re.compile(r'till'))
print(link_node.name, link_node['href'], link_node.get_text())
print('获取P段落')
p_node = soup.find('p',class_='title')#因为class是python关键字，所以要class属性要写成class_
print(p_node.name, p_node.get_text())
