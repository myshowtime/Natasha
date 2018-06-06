#-*-coding:utf-8-*-
import scrapy
class PicSpider(scrapy.Spider):
    name = "pic"
    alllowed_domains = ["27270.com"]
    def start_requests(self):
        urls = [
            'http://www.27270.com/ent/meinvtupian/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        sl = response.xpath('//div[@class="MeinvTuPianBox"]//img/@src').extract()
        yield {'image_urls':sl}
    pass