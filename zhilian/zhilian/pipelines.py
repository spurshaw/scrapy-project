# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from sql.myPymysql import DBHelper
from log.myLogging import logging_handle


# 存取到本地文件
class ZhilianPipeline(object):
    def __init__(self):
        self.f = open('job.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        jsonText = json.dumps(dict(item), ensure_ascii=False) + '\r\n'
        self.f.write(jsonText)
        return item

    def close_spider(self, spider):
        self.f.close()


# 存取到mysql数据库
class ZhilianMysqlPipeline(object):
    def __init__(self):
        self.dbhelper = DBHelper()
        self.logger = logging_handle('Pipellines')


    def process_item(self, item, spider):
        self.dbhelper.connectDatabase()
        params = (item['JobTitle'], item['company'], ','.join(item['JobTag']), item['MonthSalanry'], item['WorkPlace'], item['ReleaseData'], item['WorkNature'],
                 item['WorkExperience'], item['MinDegree'], item['RecruitingNumbers'], item['JobCategory'])
        sql = "insert into job(jobtitle, company, jobtag, monthsalary, workplace, releasedata, worknature, workexperience, mindegree, recruitingnumbers, " \
              "jobcategory) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        try:
            self.dbhelper.execute(sql, params)
            self.logger.info('insert success')
        except:
            self.logger.error('insert error')


    def close_spider(self, spider):
        try:
            self.dbhelper.close()
            self.logger.info('close mysql success')
        except:
            self.logger.error('close mysql error')




