import scrapy


class TestSpider(scrapy.Spider):
    name = 'testspider'
    start_urls = [
        'https://www.searchcraigslist.org/',
        'https://www.miss-thrifty.co.uk/',
        'https://skintdad.co.uk/',
        'https://breakingintostartups.com/',
        'https://makeawebsitehub.com/',
    ]
    list_200 = []
    list_grt_299 = []

    def parse(self, response):
        list_200 = []
        list_grt_299 = []
        if response.status in range(199, 299):
            self.list_200.append(response.url)
        else:
            self.list_grt_299.append(response.url)
        return {'success': self.list_200, 'failed': self.list_grt_299}