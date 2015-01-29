# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 14:59:31 2015

@author: Administrator
"""

import urllib                                                     #导入urllib模块
import urllib2                                                    #导入urllib2模块
import re   
import re, random, types                                                      #导入正则表达式模块：re模块
user_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0', \
           'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0', \
          'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533+ \
         (KHTML, like Gecko) Element Browser 5.0', \
         'IBM WebExplorer /v0.94', 'Galaxy/1.0 [en] (Mac OS X 10.5.6; U; en)', \
         'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)', \
         'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14', \
         'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) \
         Version/6.0 Mobile/10A5355d Safari/8536.25', \
         'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) \
         Chrome/28.0.1468.0 Safari/537.36', \
         'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; TheWorld)']

proxy = urllib2.ProxyHandler({"http":"http://127.0.0.1:8087","https":"https://127.0.0.1:8087"})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
url = 'https://scholar.google.com/scholar?hl=en&q=text+recognition&btnG=&lr=='
def getPDFFromNet(inputURL):
        request = urllib2.Request(inputURL)
        index = random.randint(0, 9)
        user_agent = user_agents[index]
        request.add_header('User-agent', user_agent)
        f = urllib2.urlopen(request)                                  #打开网页
        localDir = 'E:\github\\'                                  #下载PDF文件需要存储在本地的文件夹
        urlList = []                                              #用来存储提取的PDF下载的url的列表
        for eachLine in f:                                        #遍历网页的每一行
                line = eachLine.strip()                           #去除行首位的空格，习惯性写法
                if re.match('.*PDF.*', line):                     #去匹配含有“PDF”字符串的行，只有这些行才有PDF下载地址
                        wordList = line.split('\"')               #以"为分界，将该行分开，这样就将url地址单独分开了
                        for word in wordList:                     #遍历每个字符串
                                if re.match('.*\.pdf$', word):    #去匹配含有“.pdf”的字符串，只有url中才有
                                        urlList.append(word)      #将提取的url存入列表
        for everyURL in urlList:                                  #遍历列表的每一项，即每一个PDF的url
                wordItems = everyURL.split('/')                   #将url以/为界进行划分，为了提取该PDF文件名
                for item in wordItems:                            #遍历每个字符串
                        if re.match('.*\.pdf$', item):            #查找PDF的文件名
                                PDFName = item                    #查找到PDF文件名
                localPDF = localDir + PDFName                     #将本地存储目录和需要提取的PDF文件名进行连接
                try:                                             
                        urllib.urlretrieve(everyURL, localPDF)    #按照url进行下载，并以其文件名存储到本地目录
                except Exception, e:
                        continue

getPDFFromNet(url)