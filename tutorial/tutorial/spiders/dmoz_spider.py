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
            "http://my.yingjiesheng.com/xuanjianghui.html"
    ]
    rules = {
        'page': LinkExtractor(allow=(r'http://my.yingjiesheng.com/xjh'))
    }

    def parse(self, response):
        for link in self.rules['page'].extract_links(response):
            if link.url not in self.content_link:
                self.page_link.add(link.url)
                yield Request(link.url, callback=self.parse_item)
        next_pages = response.xpath('//*[@id="wide"]/div[4]/form/div[3]/a[12]/@href').extract()[0]
        if next_pages:
            next_page = "http://my.yingjiesheng.com" + next_pages
            self.page_link.add(next_page)
            yield Request(next_page, callback=self.parse)

    def parse_item(self, response):
        sel = Selector(response)
        items = []
        item = DmozItem()
        title = sel.xpath('//*[@id="wrap"]/div[2]/div[1]/div[1]/div[1]/text()').extract()
        desc1 = sel.xpath('//*[@id="wrap"]/div[2]/div[1]/div[3]/div[2]/div[1]/text()').extract()
        item['title'] = [t.encode('utf-8') for t in title]
        item['desc1'] = [d.encode('utf-8') for d in desc1]
        items.append(item)
        return items