import scrapy
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.signalmanager import dispatcher
from scrapy.http import HtmlResponse
from scrapy import Selector

from newspaper import Article

import logging
from datetime import datetime

class MySpider(scrapy.Spider):
    name = 'quotes_spider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath("//div[@class='quote']//span[@class='text']/text()").get()
        yield {'quotes': quotes}

class latestNews(scrapy.Spider):
    name = 'quotes_spider'
    # allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://phys.org/latest-news/']

    def parse(self, response):
        # quotes = response.css('.sorted-news-list').xpath("//a").getall()
        news_list_parsed = []
        news_list = response.css('.sorted-news-list').getall()
        for news in news_list:
            try:
                selector_news = Selector(text=news)
                # article = Article(article_url)
                # article.download().parse()

                # Get key infos fo each article from latest_news page
                article_url = selector_news.css('a.news-link::attr(href)').get()
                picture_url = selector_news.css('img::attr(src)').get()
                title = selector_news.css('a.news-link').xpath('./text()').get()
                category = selector_news.css('a.news-link::attr(href)').get()
                
                # Get key infos fo each article from each article => TRIGGER Protection
                    # authors = article.authors
                    # keywords = article.keywords
                    # publish_date = article.publish_date

                ###
                news_list_parsed.append({
                    'picture_url': picture_url, 
                    'article_url': article_url,
                    'title': title, 
                    'category': category ,
                    # 'authors' : authors,
                    # 'keywords': keywords,
                    # 'publish_date': publish_date
                    })

            except:
                print('Phys - Latest News - Getting Article Failed')

        # quotes = response.css('.sorted-news-list//.text-info').get()
        return news_list_parsed

def spider_results():
    results = []

    def crawler_results(signal, sender, item, response, spider):
        results.append(item)

    dispatcher.connect(crawler_results, signal=signals.item_passed)
    process = CrawlerProcess(get_project_settings())
    process.crawl(latestNews)
    #process.crawl(MySpider2)

    process.start()  # the script will block here until the crawling is finished
    return results

# https://phys.org/latest-news/
def latest_news():
    print('latest')


def main():
    start_time = datetime.now()
    print(spider_results())
    time_delta = datetime.now() - start_time
    execution_time = time_delta.total_seconds()
    print(execution_time )

    # get picture keywords
    # source phys.org
    return 'phys file'