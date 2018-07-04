# -*- encoding:utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from xinShengSpider.items import XinshengspiderItem

class xinSheng(CrawlSpider):
    name = 'xinsehngspider'
    allowd_domains = ["http://xinsheng.huawei.com/cn/"]
    start_urls = ['http://xinsheng.huawei.com/cn/index.php?app=forum&mod=List&act=index&class=461&p=1']

    rules=[
        Rule(LinkExtractor(allow=r"class=461&p=\d+")),
        Rule(LinkExtractor(allow=r"act=index&id=\d+"), callback="xinshengpaese")
    ]


    def xinshengpaese(self, response):
        print response.url
        item = XinshengspiderItem()

        item['title'] = response.xpath("//label[@id='topicTitle']/text()").extract()[0].strip()
        item['url'] = response.url
        item['public_time'] = response.xpath("//div[@class='bbs_info_right_pro']/span[@class='fl']/text()").extract()[0].strip()
        item['view_cnt'] = response.xpath("//span[@class='goodsee fl']/span[@class='fl']/text()").extract()[0].strip()
        item['comment_cnt'] = response.xpath("//span[@class='goodsee fl']/span[@class='fl']/text()").extract()[1].strip()
        yield item