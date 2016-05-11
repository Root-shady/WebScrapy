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
    image_path = scrapy.Field()
    size = scrapy.Field()
    image_list_path = scrapy.Field()
    color = scrapy.Field()
    group_id = scrapy.Field()
    image_urls = scrapy.Field() 
    images = scrapy.Field()

