from scrapy import Spider
from scrapy.selector import Selector
from crawler.items import CrawlerItem

class CrawlerSpider(Spider):
    name = "crawler"
    allowed_domains = ["thegioididong.com"]
    start_urls = [
        "https://www.thegioididong.com/dtdd",
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//ul[@class="homeproduct  "]/li')

        for question in questions:
            item = CrawlerItem()

            item['Title'] = question.xpath(
                'a/h3/text()').extract_first()
            item['Deal'] = question.xpath(
                'a/div[@class="price"]/strong/text()').extract_first()
            item['Real_Price'] = question.xpath(
                'a/div[@class="price"]/span/text()').extract_first()
            item['Rate'] = question.xpath(
                'a/div[@class="ratingresult"]/span/text()').extract_first()

            yield item