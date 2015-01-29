
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib2
import re, random, types
import gzip, StringIO
from bs4 import BeautifulSoup
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
#google使用
proxy = urllib2.ProxyHandler({"http":"http://127.0.0.1:8087","https":"https://127.0.0.1:8087"})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

##抓取网页
##queryStr='test'
##queryStr = urllib2.quote(queryStr)

##url = 'https://www.google.com.hk/search?hl=en&q=%s' % queryStr
url = 'https://baidu.com' 
request = urllib2.Request(url)
index = random.randint(0, 9)
user_agent = user_agents[index]
request.add_header('User-agent', user_agent)
content=urllib2.urlopen(request).read()
print content
