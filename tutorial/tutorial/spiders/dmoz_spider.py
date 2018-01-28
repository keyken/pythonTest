from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from tutorial.items import DmozItem

class DmozSpider(Spider):
    name = "dmoz"
    download_delay = 1
    allowed_domains = ["my.yingjiesheng.com"]
    page_link = set()
    content_link = set()
    start_urls = [
            "http://my.yingjiesheng.com/xjh-000-915-699.html"
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//*[@id="wrap"]/div[2]/div[1]')
        items = []
        item = DmozItem()
        title = sites.xpath('/div[1]/h2/text()').extract()
        desc1 = sites.xpath('/div[3]/div[2]/div[1]/text()').extract()
        item['title'] = [t.encode('utf-8') for t in title]
        item['desc1'] = [d.encode('utf-8') for d in desc1]
        items.append(item)
        return items
