# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhilianItem(scrapy.Item):
    JobTitle = scrapy.Field()
    company = scrapy.Field()
    JobTag = scrapy.Field()
    MonthSalanry = scrapy.Field()
    WorkPlace = scrapy.Field()
    ReleaseData = scrapy.Field()
    WorkNature = scrapy.Field()
    WorkExperience = scrapy.Field()
    MinDegree = scrapy.Field()
    RecruitingNumbers = scrapy.Field()
    JobCategory = scrapy.Field()





