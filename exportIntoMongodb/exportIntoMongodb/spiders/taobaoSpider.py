import scrapy


class TaobaospiderSpider(scrapy.Spider):
	name = 'taobaoSpider'
	allowed_domains = ['tabobao.com']
	start_urls = ['http://tabobao.com/']
	
	def parse(self, response):
		pass
