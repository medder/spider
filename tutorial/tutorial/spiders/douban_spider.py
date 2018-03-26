# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import BookItem


class BookSpider(scrapy.Spider):
    name = "book"
    start_urls = ["https://book.douban.com/"]
    allowed_domains = ["douban.com"]

    def parse(slef, response):
        s_l = response.xpath(
            '//*[@id="content"]/div/div[1]/div[1]/div[2]/div/div')
        for sel in s_l:
            sel_l = sel.xpath('ul')
            for s in sel_l:
                sel_l_ = s.xpath('li')
                for s1 in sel_l_:
                    item = BookItem()
                    item['title'] = s1.xpath('div/a/@title').extract()[
                        0].strip()
                    item['link'] = s1.xpath('div/a/img/@src').extract()[
                        0].strip()
                    item['author'] = s1.xpath(
                        'div[@class="info"]/div[@class="author"]/text()'
                    ).extract()[0].strip()
                    item['year'] = s1.xpath(
                        'div[@class="info"]/div[@class="more-meta"]/p/span[@class="year"]/text()'
                    ).extract()[0].strip()
                    item['abstract'] = s1.xpath(
                        'div[@class="info"]/div[@class="more-meta"]/p[@class="abstract"]/text()'
                    ).extract()[0].strip()
                    item['publisher'] = s1.xpath(
                        'div[@class="info"]/div[@class="more-meta"]/p/span[@class="publisher"]/text()'
                    ).extract()[0].strip()
                    yield item
