import scrapy
import time
from scrapy import signals
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from multiprocessing import Process, Queue
from crochet import setup


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = [
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
        'https://betmagician.com',
        'https://www.miss-thrifty.co.uk',
        'http://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
        'https://www.searchcraigslist.org/',
    ]

    handle_httpstatus_list = [301, 403, 404, 500, 502, 503, 504, 520, 522]

    crawled_sites = {}

    def parse(self, response):
        self.crawled_sites[response.url] = response.status


def spider_results():
    results = {}

    def collect_output(signal, response, request, spider):
        results[response.url] = response.status

    def f(q):
        try:
            process = CrawlerRunner(get_project_settings())
            crawler = process.create_crawler(BlogSpider)
            crawler.signals.connect(collect_output,
                                    signal=signals.response_received)
            d = process.crawl(crawler)
            d.addBoth(lambda _: reactor.stop())
            reactor.run()
            q.put(None)
        except Exception as e:
            q.put(e)

    q = Queue()
    p = Process(target=f, args=(q, ))
    p.start()
    result = q.get()
    p.join()

    if result is not None:
        raise result

    return results
