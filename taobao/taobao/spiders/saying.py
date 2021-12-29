import scrapy  # 引入爬虫


class sayings(scrapy.Spider):
	name = 'sayings'
	start_urls = ['http://lab.scrapyd.cn']  # 要爬取的地址数组
	
	def parse(self, response):
		saying = response.css('div.quote')[0]  # 获取到名言列表的第一部分结构
		
		text = saying.css('.text::text').extract_first()  # 获取到名言的内容
		author = saying.css('.author::text').extract_first()  # 获取到名言的作者
		tag = saying.css('.tags .tag::text').extract_first()  # 获取到名言的标签数组
		tags = tag.join(',')  # 处理标签数组为标签字符串
		
		filename = '%s-语录.txt' % author  # 爬取的内容存入文件，文件名为：作者-语录.txt
		'''
		保存文件到对应的filename文件下
		'''
		with open(filename, "a+") as f:  # 不同人的名言保存在不同的txt文档，“a+”以追加的形式
			f.write(text)
			f.write('\n')  # ‘\n’ 表示换行
			f.write('标签：' + tags)
			f.write('\n-------\n')
			f.close()
