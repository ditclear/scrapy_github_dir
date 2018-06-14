# -*- coding: utf-8 -*-
import scrapy
from ..items import ScrapyGithubDirItem


class AppSpider(scrapy.Spider):
    name = 'app'
    allowed_domains = ['github.com']
    content_domains = 'https://github.com/'
    start_urls = []

    def __init__(self, url=None, *args, **kwargs):
        super(AppSpider, self).__init__(*args, **kwargs)
        self.start_urls = [url]

    def parse(self, response):
        list = response.css('a#raw-url').xpath('@href').extract()
        if list:
            for href in list:
                href = self.content_domains+href
                print("scrapy from href --> ", href)
                yield scrapy.Request(href, callback=self.parse_link)
        else:
            for link in response.selector.xpath('//a[@class="js-navigation-open"]/@href').extract()[1:]:
                href = self.content_domains+link
                yield scrapy.Request(href, callback=self.parse)

    def parse_link(self, response):
        responseStr = str(response).strip()
        url = responseStr.strip()[5:len(responseStr)-1]
        print('download from url --> ', url)
        item = ScrapyGithubDirItem()
        item['file_urls'] = [url]
        return item
