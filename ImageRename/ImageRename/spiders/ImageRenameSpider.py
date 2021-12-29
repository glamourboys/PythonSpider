import scrapy
from ImageRename.items import ImagerenameItem

class ImagerenamespiderSpider(scrapy.Spider):
    name = 'ImageRenameSpider'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/archives/55.html',
                  'http://lab.scrapyd.cn/archives/57.html',]

    def parse(self, response):
        item = ImagerenameItem()  # 初始化对应的自定义字段
        item['imgURL'] = response.css('.post-content img::attr(src)').extract()
        item['imgName'] = response.css('.post-title a::text').extract_first()
        yield item
