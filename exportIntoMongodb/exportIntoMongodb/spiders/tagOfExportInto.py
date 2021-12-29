# -*- coding: utf-8 -*-
import scrapy  # 导入爬虫核心库
from exportIntoMongodb.items import ExportintomongodbItem  # 导入自定义参数字段
class TagInfoMongoDB(scrapy.Spider):
	name = 'TagIntomongodbspider'  # 爬虫名

	# 定义搜索入参的函数
	def start_requests(self):
		start_urls = 'http://lab.scrapyd.cn/'
		tag = getattr(self, 'tag', None)  # 加入参数搜索
		if tag is not None:
			print('13', start_urls + 'tag/' + tag)
			yield scrapy.Request(start_urls + 'tag/' + tag, callback=self.parse)
			
	def parse(self, response, **kwargs):
		lists = response.css('div.quote')  # 获取到当前页的包裹名言字段的盒子集合
		# listsLen = range(len(lists))  # 获取到该集合的范围(0[,10])
		item = ExportintomongodbItem()  # 实例化Item类
		for v in lists:
			item['content'] = v.css('.text::text').extract_first()  # 获取到名言的内容
			item['author'] = v.css('.quote.post span small::text').extract_first()  # 获取到作者的名字
			tags = v.css('.tags .tag::text').extract()  # 获取到标签数组
			item['tag'] = ','.join(tags) if len(tags) > 0 else '暂无标签'
			yield item
		# css选择器提取下一页链接
		next_page = response.css('li.next a::attr(href)').extract_first()  # 提取到下一页链接
		if next_page is not None:
			next_page = response.urljoin(next_page)
			yield scrapy.Request(next_page, callback=self.parse)