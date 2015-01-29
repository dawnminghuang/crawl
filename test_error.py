# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 09:32:15 2015

@author: Administrator
"""
from urllib2 import Request, urlopen, URLError, HTTPError

old_url = 'http://www.baidu.com'
req = Request(old_url)
response = urlopen(req)  
print 'Info():'
print response.info()
