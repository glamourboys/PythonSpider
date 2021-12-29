# 下载图片
import scrapy
from ImageSpider.items import ImagespiderItem

class ImagelabspiderSpider(scrapy.Spider):
    name = 'ImageLabSpider'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/archives/55.html']

    def parse(self, response):
        item = ImagespiderItem()  # 实例化item
        itemURLs = response.css('.post img::attr(src)').extract()  # 获取到当前路径的所有图片集合
        print(itemURLs)
        item['imgURLs'] = itemURLs
        yield item
