#!/usr/bin/env python        
# -*- coding: utf-8 -*-
"""
__title__ =  'html_outputer.py'
__author__ = 'Amanda'
__mtime__ = '2018-12-25 10:49'
__summary__ = ''
"""
import chardet


class HtmlOutputer( object ):
	def __init__(self):
		self.datas = []
	def collect_data(self, new_data):
		if new_data is None:
			return
		self.datas.append(new_data)

	def output_html(self):
		try:
			fout = open('out.html','w')
			fout.write('<html>')
			fout.write('<head>')
			fout.write('<title>')
			fout.write('Python及相关词条爬取结果')
			fout.write('</title>')
			fout.write('</head>')
			fout.write('<boby>')
			fout.write('<h1 align = "center">')
			fout.write('Python及相关词条爬取结果')
			fout.write('</h1>')
			fout.write('<table>')
			fout.write('<tr>')
			fout.write('<th>')
			fout.write('url')
			fout.write('</th>')
			fout.write('<th>')
			fout.write('title')
			fout.write('</th>')
			fout.write('<th>')
			fout.write('summary')
			fout.write('</th>')
			fout.write('</tr>')
			for data in self.datas:
				fout.write('<tr>')
				fout.write('<td>%s</td>' % data['url'])
				#encode_type =chardet.detect(data['title'])
				#title = data['title'].decode(encode_type['encoding'])
				fout.write('<td>%s</td>' % data['title'])
				#encode_type =chardet.detect(data['summary'])
				#summary = data['summary'].decode(encode_type['encoding'])
				fout.write('<td>%s</td>' % data['summary'])
				fout.write('</tr>')
				fout.write('</table>')
				fout.write('</boby>')
				fout.write('</html>')
		except Exception as e:
			print("output the crawl test catch error:", e)
		finally:
			fout.close()
