import scrapy


class NbaScrapingProjectSpider(scrapy.Spider):
    name = "NBA_scraping_project"
    allowed_domains = ["www.nba.com"]
    start_urls = ["https://www.nba.com/stats"]

    def parse(self, response):
        pass
