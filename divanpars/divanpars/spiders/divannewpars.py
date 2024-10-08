import scrapy

import scrapy
import csv

class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/rostov-na-donu/category/divany-i-kresla"]

    # Инициализация списка для хранения данных
    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'price.csv',
        'FEED_EXPORT_ENCODING': 'utf-8'  # Установка кодировки UTF-8
    }

    def parse(self, response):
        divans = response.css('div._Ud0k')
        for divan in divans:
            yield {
                'price': divan.css('div.pY3d2 span::text').get(),
            }
'''
============================================================
    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'price.csv',
        'FEED_EXPORT_FIELDS': ['price'],
    }

    def parse(self, response):
        divans = response.css('div._Ud0k')
        if not divans:
            self.logger.warning("Не удалось найти диваны. Проверьте селекторы.")
        for divan in divans:
            price = divan.css('div.pY3d2 span::text').get()
            if price:
                yield {'price': price}
            else:
                self.logger.warning("Цена не найдена для одного из диванов.")
'''