import scrapy
from urllib.parse import urljoin


class sayinglistall(scrapy.Spider):
	name = 'sayinglistall'
	start_urls = ['http://lab.scrapyd.cn']  # 要爬取的地址数组'
	
	# 声明函数
	def parse(self, response):
		lists = response.css('div.quote')  # 获取到名言列表结构
		listsNum = range(len(lists))  # 获取到要使用列表的总长度
		for index in listsNum:
			text = lists[index].css('.text::text').extract_first()  # 获取到名言的内容
			author = lists[index].css('.author::text').extract_first()  # 获取到名言的作者
			tags = lists[index].css('.tags .tag::text').extract()  # 获取到名言的标签数组
			tag = ','.join(tags) if len(tags) > 0 else '暂无标签'  # 处理标签数组为标签字符串 写法: 默认值  if 条件 else 其他值  =>  满足条件时返回:默认值;不满足时返回:其他值
			filename = '%s-语录.txt' % author   # 爬取的内容存入文件，文件名为：作者-语录.txt
			'''
			保存文件到对应的filename文件下
			a+ :追加
			'''
			with open(filename, "a+") as f:  # 不同人的名言保存在不同的txt文档，“a+”以追加的形式
				f.write('\n---------\n')
				f.write(text)
				f.write('\n')  # ‘\n’ 表示换行
				f.write('标签：' + tag)
				f.write('\n')
				f.write('作者：' + author)
				# f.close()
		next_page = response.css('li.next a::attr(href)').extract_first()  # 获取到下一页的路径链接
		if next_page is not None:
			next_page = response.urljoin(next_page)
			yield scrapy.Request(next_page, callback=self.parse)