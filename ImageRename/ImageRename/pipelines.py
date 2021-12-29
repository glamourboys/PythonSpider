# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
import re

class ImagerenamePipeline(ImagesPipeline):
    # 这个函数是下载函数
    def get_media_requests(self, item, spider):
        for imgURL in item['imgURL']:
            yield Request(imgURL, meta={'name': item['imgName']})
      
    # 函数自带,此处重写文件处理函数
    def file_path(self, request, response=None, info=None):
        imgName = request.url.split('/')[-1]  # 剪切到url的图片名称
        name = request.meta['name']
        name = re.sub(r'[？\\*|“<>:/]', '', name)
        filename = u'{0}\{1}'.format(name, imgName)
        print('pipelines', imgName, name)
        return filename