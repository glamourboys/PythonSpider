# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class ImagespiderPipeline(ImagesPipeline):
    def get_media_requests(self, item, spider):
        for imgURL in item['imgURLs']:
            yield Request(imgURL)
            # return imgURL
    def file_path(self, request, response=None, info=None):
        # 重命名，若不重写这函数，图片名为哈希，就是一串乱七八糟的名字
        image_guid = request.url.split('/')[-1]  # 提取url前面名称作为图片名。
        return image_guid