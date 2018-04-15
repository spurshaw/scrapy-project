# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import json
import codecs


class LianjiaLinkPipeline(object):
    def __init__(self):
        # 创建一个文件
        self.filename = codecs.open("lianjia.json", "w", encoding = "utf-8")

    def process_item(self, item, spider):
        # 中文默认使用ascii码来存储，禁用后默认为Unicode字符串
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.filename.write(content)
        return item

    def close_spider(self, spider):
        self.filename.close()