# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    title = scrapy.Field()  # 书名
    link = scrapy.Field()  # 封面地址
    author = scrapy.Field()  # 作者
    year = scrapy.Field()  # 年份
    abstract = scrapy.Field()  # 概要
    publisher = scrapy.Field()  # 出版社
