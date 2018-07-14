# -*- encoding:utf-8 -*-

import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from xinShengSpider.items import XinshengspiderItem
from scrapy_redis.spiders import RedisCrawlSpider


class xinSheng(RedisCrawlSpider):
    name = 'xinsehngspider'
    # allowd_domains = ["http://xinsheng.huawei.com/cn/"]
    redis_key = "xinshengspider:start_urls"

    # 动态域范围获取
    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(xinSheng, self).__init__(*args, **kwargs)

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

        lst = [1,2,3,3,5,7]
        s = [lst[i+1]-lst[i] for i in range(0,len(lst)-1)]
        s = map(lambda x,y: x-y, lst[:1],lst[:-1])