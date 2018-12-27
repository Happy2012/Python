#!/usr/bin/env python        
# -*- coding: utf-8 -*-
"""
__title__ =  'test_urllib_request.py'
__author__ = 'Amanda'
__mtime__ = '2018-12-24 11:58'
__summary__ = '网页下载的三种方法'
"""
import urllib.request
import http.cookiejar

url = "http://www.baidu.com"
print("第一种方法")
response1 = urllib.request.urlopen(url)
print(response1.getcode())
print(len(response1.read()))
print("第二种方法")
request = urllib.request.Request(url)
request.add_header("user-agent","Mozilla/5.0")
response2 = urllib.request.urlopen(request)
print(response2.getcode())
print(len(response2.read()))
print("第三种方法")
cj = http.cookiejar.CookieJar()
pro = urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(pro)
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)
print(response3.getcode())
print(cj)
print('cookie对象打印完毕\n')
print(response3.read())
