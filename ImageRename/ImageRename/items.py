# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImagerenameItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    imgURL = scrapy.Field()  # 图片路径
    imgName = scrapy.Field()  # 图片名称
 