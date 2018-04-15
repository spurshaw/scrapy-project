# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
from selenium import webdriver
from scrapy.http import HtmlResponse

# user-agent池
user_agent = [
    "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1",
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)"
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
]

# 随机获取user-agent
class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        userAgent = random.choice(user_agent)
        print(userAgent)
        request.headers.setdefault('User-Agent', userAgent)


# 处理动态网页方式
class PhantomJSMiddleware(object):
    def process_request(self, request, spider):
        driver = webdriver.PhantomJS(r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
        driver.get(request.url)
        content = driver.page_source.encode('utf-8')
        driver.quit()
        return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)


