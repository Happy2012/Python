#!/usr/bin/env python        
# -*- coding: utf-8 -*-
"""
__title__ =  'html_downloader.py'
__author__ = 'Amanda'
__mtime__ = '2018-12-25 10:48'
__summary__ = ''
"""
import urllib.request

import chardet


class HtmlDownloader( object ):
	def download(self, url):
		if url is None:
			return
		response = urllib.request.urlopen(url)
		if response.getcode() != 200:
			return
		html = response.read()
		encode_type = chardet.detect(html)
		html = html.decode(encode_type['encoding'])#对html进行解码将其从bytes类型转成string类型
		return html
