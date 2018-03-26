# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb


class MySQLStorePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(
            'localhost',
            'root',
            '',
            'my_test',
            charset="utf8",
            use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                """INSERT INTO book_store (title, link, author, year, abstract, publisher)
                            VALUES (%s, %s, %s, %s, %s, %s)""",
                (item['title'].encode('utf-8'), item['link'].encode('utf-8'),
                 item['author'].encode('utf-8'), item['year'].encode('utf-8'),
                 item['abstract'].encode('utf-8'),
                 item['publisher'].encode('utf-8')))

            self.conn.commit()

        except Exception as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

        return item
