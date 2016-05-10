# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ClothItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
    item_code = scrapy.Field()
    trace = scrapy.Field()
    image = scrapy.Field()
    size = scrapy.Field()
    detail_image = scrapy.Field()
    color = scrapy.Field()
    group_id = scrapy.Field()

