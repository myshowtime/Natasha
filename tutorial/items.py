# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class MyItem(scrapy.Item):
    image_urls = scrapy.Field()  #保存图片地址
    images = scrapy.Field()      #保存图片的信息
    pass