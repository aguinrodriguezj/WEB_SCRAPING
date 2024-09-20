import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'example'
    custom_settings = {
        'REQUEST_FINGERPRINTER_IMPLEMENTATION': '2.7',
        'ROBOTSTXT_OBEY': True, # validamos el archivo robots.txt
        'FEED_EXPORT_ENCODING': 'utf-8' # codificación usada en la exportación
    }
    start_urls = ['https://www.amazon.es/']

    def parse(self, response):
        # Usamos selectores CSS o XPath para extraer el título
        for title in response.css('title::text'):
            yield {'title': title.get()}