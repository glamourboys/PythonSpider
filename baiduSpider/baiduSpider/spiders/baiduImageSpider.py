import scrapy
from baiduSpider.items import BaiduspiderItem

class BaiduimagespiderSpider(scrapy.Spider):
    name = 'baiduImageSpider'
    allowed_domains = ['image.baidu.com']
    start_urls = ['https://image.baidu.com/search/albumsdetail?tn=albumsdetail&word=蛋糕&fr=albumslist&album_tab=人物&album_id=170&rn=30']
    # https://image.baidu.com/search/albumslist?tn=albumslist&word=%E8%9B%8B%E7%B3%95&album_tab=%E4%BA%BA%E7%89%A9&rn=15&fr=albumsdetail_nav
    # https://image.baidu.com/search/albumslist?tn=albumslist&word=%E8%9B%8B%E7%B3%95&album_tab=%E4%BA%BA%E7%89%A9&rn=15&fr=albumsdetail_nav
    def parse(self, response):
        item = BaiduspiderItem()  # 初始化自定义字段
        imgList = response.css('#imgList img::attr(src)').extract()
        item['imgURL'] = imgList
        yield item
