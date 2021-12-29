# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymongo  # 链接mongodbd插件

class ExportintomongodbPipeline:
    # 初始函数
    def __init__(self):
        # 链接数据库
        client = pymongo.MongoClient('127.0.0.1', 27017)  # 创建链接
        # 连接所需数据库名
        db = client['MingYanTag']
        # 连接对应的库表
        self.post = db['mingyan']
    
    def process_item(self, item, spider):
        postItem = dict(item)  # 转化为字典形式
        self.post.insert(postItem)  # 向表中插入一条数据
        return item  # 可以输出到控制台,可以不写
