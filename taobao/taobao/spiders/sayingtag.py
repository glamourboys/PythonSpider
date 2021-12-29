import scrapy
# http://lab.scrapyd.cn/tag/名画/

class sayingtag(scrapy.Spider):
	name = 'sayingtag'
	
	# 新增的代码,实现传参爬取
	
	def start_requests(self):
		start_urls = 'http://lab.scrapyd.cn/'  # 基础路径
		tag = getattr(self, 'tag', None)  # 加入参数搜索
		if tag is not None:
			yield scrapy.Request(start_urls + 'tag/' + tag, callback=self.parse)
		
	'''
	以下内容为原始代码,无变化!
	'''
	
	def parse(self, response):
		lists = response.css('div.quote')  # 获取当前列表盒子集合
		listsLen = range(len(lists))  # 获取到当前页列表盒子的长度范围
		for index in listsLen:
			text = lists[index].css('.text::text').extract_first()  # 获取到名言的实体内容
			author = lists[index].css('.quote.post span small::text').extract_first()  # 获取到对应的作者名字
			tags = lists[index].css('.tags .tag::text').extract()  # 获取到标签数组
			tag = ','.join(tags)  # 数组转换为字符串
			filename = '%s -标签语录.txt' % tag
			
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
				f.close()
		next_page = response.css('li.next a::attr(href)').exarct_first()  # 获取到点击下一页的按钮
		if next_page is not None:  # 判断下一页是否为空
			scrapy.Request(next_page, callback=self.parse)
			
			
	# scrapy crawl argsSpider -a tag=爱情