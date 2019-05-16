# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


class MysqlPipeline(object):
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('HOST'),
            username=crawler.settings.get('USERNAME'),
            password=crawler.settings.get('PASSWORD'),
            database=crawler.settings.get('DATABASE'))

    def open_spider(self, spider):
        self.db = pymysql.connect(
            self.host,
            self.username,
            self.password,
            self.database,
            charset='utf8')
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()

    def process_item(self, item, spider):
        sql = 'insert into scrapy_quotes (author, tags, text) values ("{author}", "{tags}", "{text}")'.format(
            author=item['author'], tags=item['tags'], text=item['text'])
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()