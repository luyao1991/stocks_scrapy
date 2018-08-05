# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class StocksScrapyPipeline(object):
    def process_item(self, item, spider):
        return item

# 需要到settings里面找到ITEM_PIPELINES，配置这个类
class StocksScrapyInfoPipeline(object):
    # 定义所需的三个方法
    def open_spider(self,spider):
        self.f = open('baidu_stocks.txt','w')

    def close_spider(self,spider):
        self.f.close()

    def process_item(self,item,spider):
        try:
            line = str(dict(item)) + '\n'
            self.f.write(line)
        except:
            pass
        return item
