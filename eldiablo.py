# NOMBRE_DEL_DUEÑO_CODIGO: AnaGomez123
# TEMATICA_DEL_CODIGO: Web scraping con Scrapy
# IEM_ESCUELA_NORMAL_PASTO: IEM Normal de Pasto
# CURSO: Programación Web

import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['http://example.com']

    def parse(self, response):
        title = response.css('h1::text').get()
        print("Title:", title)

        links = response.css('a::attr(href)').getall()
        print("Links:", links)

process = scrapy.CrawlerProcess()
process.crawl(MySpider)
process.start()
