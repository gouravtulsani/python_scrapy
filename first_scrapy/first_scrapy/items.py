# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class First_scrapyItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    desc = scrapy.Field()