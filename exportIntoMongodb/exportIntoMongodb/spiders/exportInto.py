# -*- coding: utf-8 -*-
import scrapy  # 导入核心

from exportIntoMongodb.items import ExportintomongodbItem  # 导入要查询的参数

class Intomongodbspider(scrapy.Spider):
	name = 'Intomongodbspider'  # 爬虫名字
	allowed_domains = ["lab.scrapyd.cn"]
	start_urls = ['http://lab.scrapyd.cn/']
	
	'''
	定义函数:取到需要的文字
	'''
	def parse(self, response, **kwargs):
		sayings = response.css('div.quote')  # 取到整页的名言盒子
		item = ExportintomongodbItem()  # 实例化Item类
		# 提取名言
		for v in sayings:
			item['content'] = v.css('.text::text').extract_first()  # 提取名言内容
			item['author'] = v.css('.quote.post span small::text').extract_first()  # 提取名言内容
			tag = v.css('.tags .tag::text').extract()  # 提取到标签数组
			item['tag'] = ','.join(tag) if len(tag) > 0 else '暂无标签'  # 标签
			# 弹出该item对象 把取到的内容提交到 pipeline 处理
			yield item
		# css选择器提取下一页链接
		next_page = response.css('li.next a::attr(href)').extract_first()  # 提取到下一页链接
		if next_page is not None:
			next_page = response.urljoin(next_page)
			yield scrapy.Request(next_page, callback=self.parse)