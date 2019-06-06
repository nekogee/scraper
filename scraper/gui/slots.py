import spiders.mySpider
from scrapy import cmdline

def buttonSendUrl(self, url):
    spiders.mySpider.MyspiderSpider.start_urls.clear()
    spiders.mySpider.MyspiderSpider.start_urls.append(url)
    spiders.mySpider.MyspiderSpider.allowed_domains.clear()
    spiders.mySpider.MyspiderSpider.allowed_domains.append(url)
    print(url)
    cmdline.execute('scrapy crawl mySpider'.split())


