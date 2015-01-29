
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2, socket, time
import gzip, StringIO
import re, random, types
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



localDir = 'E:\github\\' 
PDFName= 'text detection'

##解析google的搜索结果，下载PDF文件

    ##登陆google需要开启代理
proxy = urllib2.ProxyHandler({"http":"http://127.0.0.1:8087","https":"https://127.0.0.1:8087"})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
url = 'http://scholar.google.com/scholar?hl=en&q=Text+detection+in+indoor%2Foutdoor+scene+images&btnG=&as_sdt=1%2C5&as_sdtp='
request = urllib2.Request(url)
index = random.randint(0, 9)
user_agent = user_agents[index]
request.add_header('User-agent', user_agent)
    ##匹配正则表达式
try :
     result = urllib2.urlopen(request)
except urllib2.URLError,e :
    if hasattr(e, "code"):
        print "The server couldn't fulfill the request."
        print "Error code: %s" % e.code
    elif hasattr(e, "reason"):
        print "We failed to reach a server. Please check your url and read the Reason"
        print "Reason: %s" % e.reason
    sys.exit(2)
content = result.read().decode("utf-8")
        # with open("page.html", "w") as my_file :
        #     my_file.write(content)
print "读取网页成功..."
        #content = content.decode("utf-8")
down_pdfs = re.findall(r'<a.*?href="(.*?pdf)"', content)
print "正则匹配结束..."

for everyURL in down_pdfs:
    print everyURL
    localPDF = localDir + PDFName                     #将本地存储目录和需要提取的PDF文件名进行连接
    try:                                             
        urllib.urlretrieve(everyURL, localPDF)    #按照url进行下载，并以其文件名存储到本地目录
    except Exception,e:
        continue
print "下载结束..."