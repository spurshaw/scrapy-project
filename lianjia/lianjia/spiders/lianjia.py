# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from LianJia.items import LianjiaLinkItem, HouseItem


class LianjiaSpider(CrawlSpider):
    name = 'lianjia'
    allowed_domains = ['wh.lianjia.com']
    start_urls = ['https://wh.lianjia.com/ershoufang/pg1/']
    rules = [
        Rule(LinkExtractor(allow=r'https://wh.lianjia.com/ershoufang/pg1/'), callback='link_parse'),
        Rule(LinkExtractor(allow=r'ershoufang/\d+.html'), callback='house_parse'),
    ]

    def house_parse(self, response):
        print(response.request)
        print(response.url)
        print(response.status)
        item = HouseItem()
        HouseTitle = response.xpath("//div[@class='title']/h1/text()").extract()[0]
        item['HouseTitle'] = HouseTitle
        HousePrice = response.xpath("//div[@class='overview']/div[2]/div[2]/span[1]/text()").extract()[0]
        item['HousePrice'] = HousePrice
        HouseUnitPrice = response.xpath("//div[@class='overview']/div[2]/div[2]/div[1]/div[1]/span/text()").extract()[0]
        item['HouseUnitPrice'] = HouseUnitPrice
        DownPay = response.xpath("//div[@class='tax']/span[@class='taxtext']/span/text()").extract()[0]
        item['DownPay'] = DownPay
        TaxesFees = response.xpath("//div[@class='tax']/span[@class='taxtext']/span[3]/span/text()").extract()[0]
        item['TaxesFees'] = TaxesFees
        VillageName = response.xpath("//div[@class='aroundInfo']/div[1]/a[1]/text()").extract()[0]
        item['VillageName'] = VillageName
        Area = response.xpath("//div[@class='aroundInfo']/div[2]/span[2]/a/text()").extract()[0]
        item['Area'] = Area
        Location = response.xpath("//div[@class='aroundInfo']/div[2]/span[2]/a/text()").extract()[1]
        item['Location'] = Location
        Subway = response.xpath("//div[@class='aroundInfo']/div[2]/a/text()").extract()
        if Subway:
            item['Subway'] = Subway[0]
        else:
            item['Subway'] = None
        ConstructionTime = response.xpath("//div[@class='houseInfo']/div[3]/div[2]/text()").extract()[0]
        item['ConstructionTime'] = ConstructionTime
        HouseType = response.xpath("//div[@class='base']/div[2]/ul/li[1]/text()").extract()[0]
        item['HouseType'] = HouseType
        CurrentFloor = response.xpath("//div[@class='base']/div[2]/ul/li[2]/text()").extract()[0]
        item['CurrentFloor'] = CurrentFloor
        BulidArea = response.xpath("//div[@class='base']/div[2]/ul/li[3]/text()").extract()[0]
        item['BulidArea'] = BulidArea
        BuildingHead = response.xpath("//div[@class='base']/div[2]/ul/li[7]/text()").extract()[0]
        item['BuildingHead'] = BuildingHead
        DecorateSituation = response.xpath("//div[@class='base']/div[2]/ul/li[9]/text()").extract()[0]
        item['DecorateSituation'] = DecorateSituation
        EquippedElevator = response.xpath("//div[@class='base']/div[2]/ul/li[11]/text()").extract()[0]
        item['EquippedElevator'] = EquippedElevator
        ListedTime = response.xpath("//div[@class='transaction']/div[2]/ul/li[1]/span[2]/text()").extract()[0]
        item['ListedTime'] = ListedTime
        HouseUse = response.xpath("//div[@class='transaction']/div[2]/ul/li[4]/span[2]/text()").extract()[0]
        item['HouseUse'] = HouseUse
        FixedNumber = response.xpath("//div[@class='transaction']/div[2]/ul/li[5]/span[2]/text()").extract()[0]
        item['FixedNumber'] = FixedNumber
        HouseTag = response.xpath("//div[@class='tags clear']/div[2]/a/text()").extract()
        item['HouseTag'] = HouseTag

        yield item

        def link_parse(self, response):
            for each in response.xpath("//div[@class='leftContent']/ul/li/a/@href"):
                item = LianjiaLinkItem()
                link = each.extract[0]
                print(link)
                item['Link'] = link

                yield item
