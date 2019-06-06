# -*- coding: utf-8 -*-
import scrapy


class MyspiderSpider(scrapy.Spider):
    name = 'mySpider'
    allowed_domains = ['www.scut.edu.cn/']
    start_urls = ['https://www.scut.edu.cn/new/']

    def parse(self, response):
        pass
