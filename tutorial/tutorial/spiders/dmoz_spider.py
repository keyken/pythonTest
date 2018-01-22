from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import Request

from tutorial.items import DmozItem

class DmozSpider(Spider):
    name = "dmoz"
    download_delay = 1
    allowed_domains = ["zhaopin.baidu.com"]
    start_urls = [
        "http://zhaopin.baidu.com/xzzw?detailidx=0&city=%E5%B9%BF%E5%B7%9E&id=http%3A%2F%2Fwww.wutongguo.com%2Fnotice9627E8649A.html%3Furl_id%3D4&query=%E5%BA%94%E5%B1%8A%E7%94%9F%E6%8B%9B%E8%81%98"
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('/html/body/div[3]/div[1]')
        item = DmozItem()
        url1 = str(response.url)
        title = sites.xpath('div[3]/div[1]/span/text()').extract()
        desc1 = sites.xpath('div[4]/div[1]/div/div[1]/div[1]/div/p/text()').extract()

        item['title'] = [t.encode('utf-8') for t in title]
        item['desc1'] = [d.encode('utf-8') for d in desc1]
        item['url1'] = url1.encode('utf-8')

        yield item

        urls = sel.xpath('/html/body/div[3]/div[1]/div[4]/div[1]/div/div[1]/div[3]/a/@href').extract()
        for url in urls:
            url = "http://zhaopin.baidu.com" + url
            yield Request(url, callback=self.parse)