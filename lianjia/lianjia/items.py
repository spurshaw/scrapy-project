# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaLinkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Link = scrapy.Field()


class HouseItem(scrapy.Item):
    HouseTitle = scrapy.Field()
    HousePrice = scrapy.Field()
    HouseUnitPrice = scrapy.Field()
    DownPay = scrapy.Field()
    TaxesFees = scrapy.Field()
    VillageName = scrapy.Field()
    Area = scrapy.Field()
    Location = scrapy.Field()
    Subway = scrapy.Field()
    ConstructionTime = scrapy.Field()
    HouseType = scrapy.Field()
    CurrentFloor = scrapy.Field()
    BulidArea = scrapy.Field()
    BuildingHead = scrapy.Field()
    DecorateSituation = scrapy.Field()
    EquippedElevator = scrapy.Field()
    ListedTime = scrapy.Field()
    HouseUse = scrapy.Field()
    FixedNumber = scrapy.Field()
    HouseTag = scrapy.Field()




