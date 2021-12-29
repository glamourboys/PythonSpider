import scrapy


class WangzhearmsSpider(scrapy.Spider):
    name = 'WangzheArms'
    start_urls = ['https://pvp.qq.com/web201605/item.shtml']

    def parse(self, response):
        parentTabS = response.css('.parent-type label::text').extract()
        secondTabs = response.css('.sub-type label::text').extract_first()
        print(parentTabS, secondTabs)
        pass
