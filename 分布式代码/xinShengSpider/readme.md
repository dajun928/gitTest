采用分布式爬取华为家事信息
	1.reids主机为120.78.198.108
	2.在执行爬虫的服务器上CMD执行：scrapy runspider xinsheng.py，开启爬虫监听
	3.在120.78.198.108上push任务初始url：lpush xinshengspider:start_urls http://xinsheng.huawei.com/cn/index.php?app=forum&mod=List&act=index&class=461