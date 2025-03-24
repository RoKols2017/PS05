import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://www.divan.ru/sankt-peterburg/"]
    start_urls = ["https://www.divan.ru/sankt-peterburg/category/divany-i-kresla"]

    def parse(self, response):
        divans = response.css('div.Pk6w8')
        for divan in divans:
            yield {
                'name' : divan.css('div.q5Uds span::text').get()
            }