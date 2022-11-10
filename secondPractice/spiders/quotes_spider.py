import scrapy
from ..items import SecondpracticeItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    # quotes= ''
    start_urls = [
        "https://quotes.toscrape.com/"
    ]
    allowed_domains = ["quotes.toscrape.com"]

    def parse(self,response):
        all_div_quotes = response.css('div.quote')
        for quote in all_div_quotes:
            items = SecondpracticeItem()

            title = quote.css('span.text::text').getall()
            author = quote.css('.author::text').getall()
            tag = quote.css('.tag::text').getall()
            
            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            yield items
            
        next_page = response.css('.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)

            

            