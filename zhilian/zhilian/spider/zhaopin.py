# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider
from zhilian.items import ZhilianItem
from log.myLogging import logging_handle

logger = logging_handle('zhaopin')


class ZhaopinSpider(RedisCrawlSpider):
    name = 'zhaopin'
    allowed_domains = ['zhaopin.com']
    # start_urls = ['http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%AD%A6%E6%B1%89&p=1&isadv=0']
    redis_key = "zhaopinspider:start_urls"
    rules = (
        # 匹配武汉各区 jl=%E6%AD%A6%E6%B1%89代表武汉
        Rule(LinkExtractor(allow=r'/jobs/searchresult.ashx\?jl=%E6%AD%A6%E6%B1%89&isadv=0&isfilter=1&p=1&re=\d+'),
             callback='wuhan_parse', follow=True),
        # 匹配页码
        Rule(LinkExtractor(allow=r'/jobs/searchresult.ashx\?jl=%e6%ad%a6%e6%b1%89&isadv=0&isfilter=1&re=\d+&sg=\w+&p=\d+'),
             callback='wuhan_parse', follow=True),
        # 匹配具体页面
        Rule(LinkExtractor(allow=r'http://jobs.zhaopin.com/\d+.htm'), callback='work_parse', follow=False)
    )

    def wuhan_parse(self, response):
        print(response.url)
        print(response.status)
        logger.info('Link：' + response.url)
        logger.info('Link：' + str(response.status))

    def work_parse(self, response):
        print(response.url)
        print(response.status)
        logger.info('url：' + response.url)
        logger.info('url：'+ str(response.status))
        item = ZhilianItem()
        item['JobTitle'] = response.xpath("//div[@class='fixed-inner-box']/div[1]/h1/text()").extract()[0]
        item['company'] = response.xpath("//div[@class='fixed-inner-box']/div[1]/h2/a/text()").extract()[0]
        item['JobTag'] = response.xpath("//div[@class='fixed-inner-box']/div[1]/div[1]/span/text()").extract()
        item['MonthSalanry'] = response.xpath("//div[@class='terminalpage-left']/ul/li[1]/strong/text()").extract()[0]
        item['WorkPlace'] = response.xpath("//div[@class='terminalpage-left']/ul/li[2]/strong/a/text()").extract()[0]
        item['ReleaseData'] = response.xpath("//div[@class='terminalpage-left']/ul/li[3]/strong/span/text()").extract()[0]
        item['WorkNature'] = response.xpath("//div[@class='terminalpage-left']/ul/li[4]/strong/text()").extract()[0]
        item['WorkExperience'] = response.xpath("//div[@class='terminalpage-left']/ul/li[5]/strong/text()").extract()[0]
        item['MinDegree'] = response.xpath("//div[@class='terminalpage-left']/ul/li[6]/strong/text()").extract()[0]
        item['RecruitingNumbers'] = response.xpath("//div[@class='terminalpage-left']/ul/li[7]/strong/text()").extract()[0]
        item['JobCategory'] = response.xpath("//div[@class='terminalpage-left']/ul/li[8]/strong/a/text()").extract()[0]

        yield item

