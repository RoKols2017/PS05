import scrapy

class DivanSpider(scrapy.Spider):
    name = "divan"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/sankt-peterburg/category/svet"]

    def parse(self, response):
        # Используем более надежные селекторы для выбора элементов товаров
        products = response.css('div.lsooF')

        for product in products:
            yield {
                "title": product.css('span::text').get(),
                "price": product.css("span.product-price::text").get(),
                "link": response.urljoin(product.css("a.product-title::attr(href)").get())
            }

        # Пагинация: ищем ссылку на следующую страницу и переходим
        next_page = response.css("a.next-page::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)
