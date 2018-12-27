#!/usr/bin/env python        
# -*- coding: utf-8 -*-
"""
__title__ =  'html_parser.py'
__author__ = 'Amanda'
__mtime__ = '2018-12-25 10:48'
__summary__ = ''
"""
import re
from bs4 import BeautifulSoup
import urllib.parse

class HtmlParser( object ):
	def parse(self, page_url, html_content):
		if page_url is None or html_content is None:
			return
		#soup = BeautifulSoup(html_content,'html.parser')
		soup = BeautifulSoup(html_content,'html.parser',from_encoding='Unicode')
		new_urls = self._get_new_urls( page_url, soup )
		new_data = self._get_new_data(page_url, soup)
		return new_urls, new_data

	def _get_new_urls(self, page_url, soup):
		new_urls = set()
		links = soup.find_all('a', href = re.compile(r'/item/.+'))
		for link in links:
			new_url = link['href']
			new_full_url = urllib.parse.urljoin(page_url, new_url)#将new_url按page_url格式拼接成一个完整的url
			new_urls.add(new_full_url)
		return new_urls

	def _get_new_data(self, page_url, soup):
		res_data = {}
		res_data['url'] = page_url
		#root_url = 'https://baike.baidu.com/item/python/407313'
		#<dd class="lemmaWgt-lemmaTitle-title">
			#<h1>Python</h1>
		title_node = soup.find('dd', class_ = 'lemmaWgt-lemmaTitle-title').find('h1')
		res_data['title'] = title_node.get_text()
		"""
		<div class="lemma-summary" label-module="lemmaSummary">
			<div class="para" label-module="para">Python是一种计算机程序设计语言。是一种动态的、面向对象的脚本语言，最初被设计用于编写自动化脚本(shell)，随着版本的不断更新和语言新功能的添加，越来越多被用于独立的、大型项目的开发。</div>
		</div>
		"""
		summary_node = soup.find('div', class_ = "lemma-summary")
		res_data['summary'] = summary_node.get_text()
		return  res_data



