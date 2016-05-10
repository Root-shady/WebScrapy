# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import MySQLdb
from twisted.enterprise import adbapi


class UniqloPipeline(object):
    def process_item(self, item, spider):
        return item
class MySQLStorePipeLine(object):
    """
    A pipeline to store the item in a MySQL database
    """
    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        dbargs = dict(
                host = settings['MYSQL_HOST'],
                db = settings['MYSQL_DBNAME'],
                user = settings['MYSQL_USER'],
                passwd = settings['MYSQL_PASSWD'],
                charset = 'utf8',
                use_unicode = True
            )
        conn = MySQLdb.connect(**dbargs)
        return cls(conn)


    def __init__(self, conn):
        #self.conn = MySQLdb.connect(user='root', passwd = '6566619', db = 'webScrape',
        #        host='localhost', charset='utf8', use_unicode=True,)
        self.conn = conn
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            sql =  """INSERT INTO uniqlo VALUES(null, "%s", "%s", %f, "%s", "%s", "%s", "%s", "%s", "%s", %d);""" % (item['title'], item['description'], float(item['price']), item['item_code'], item['trace'], item['image'], item['size'],item['color'], item['detail_image'], item['group_id'])

            self.cursor.execute(sql)
            self.conn.commit()
        except MySQLdb.Error, e:
            print("Error while insert into database", e)
        return item
    def close_spider(self, spider):
        self.conn.close()


