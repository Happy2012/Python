#!/usr/bin/env python        
# -*- coding: utf-8 -*-
"""
__title__ =  'spider_main.py'
__author__ = 'Amanda'
__mtime__ = '2018-12-25 10:47'
__summary__ = '爬取百度百科python词条，以及该词条引用到的其他词条(最多爬1000就停止爬取)'
"""
import datetime

from baike_spider import html_downloader, url_manager, html_parser, html_outputer


class SpiderMain( object ):
		def __init__(self):
			self.urls = url_manager.UrlManager()
			self.dowloader = html_downloader.HtmlDownloader()
			self.parser = html_parser.HtmlParser()
			self.outputer = html_outputer.HtmlOutputer()

		def crawl(self, root_url):
			count = 1
			self.urls.add_new_url(root_url)
			while self.urls.has_new_url():
				try:
					new_url = self.urls.get_new_url()
					print('crawl %d : %s' % (count, new_url))
					html_content = self.dowloader.download( new_url )
					new_urls, new_data = self.parser.parse( new_url, html_content )
					self.urls.add_new_urls( new_urls )
					self.outputer.collect_data( new_data )
					if count == 20:
						break
				except Exception as e:
					print('crawl failed:%s' % e)
				count += 1
			self.outputer.output_html()

if __name__ == '__main__':
	root_url = 'https://baike.baidu.com/item/python/407313'
	obj_spider = SpiderMain()
	btime = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S')
	print('crawl begin at:',btime)
	obj_spider.crawl(root_url)
	etime = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S')
	print('crawl end at:', etime)
	print('crawl is last from %s to %s' % (btime,etime))
