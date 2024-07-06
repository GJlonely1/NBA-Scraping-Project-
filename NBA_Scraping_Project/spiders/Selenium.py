import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from scrapy import signals
from scrapy.http import HtmlResponse

class NbaScrapingProjectSpiderSelenium(scrapy.Spider):
    name = "NBA_scraping_project_selenium"
    allowed_domains = ["basketball-reference.com"]
    start_urls = ["https://www.basketball-reference.com/leagues/NBA_2024_totals.html"]
    
    def __init__(self, *args, **kwargs):
        super(NbaScrapingProjectSpiderSelenium, self).__init__(*args, **kwargs)
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(NbaScrapingProjectSpiderSelenium, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        spider.driver.quit()

    def parse(self, response):
        self.driver.get(response.url)
        self.human_behaviour()

        stats_choice_all = self.driver.find_elements(By.CSS_SELECTOR, "div.filter div")
        year_choices_sideurl = self.driver.find_elements(By.CSS_SELECTOR, "div.prevnext a")
        year_to_select_sideurl = year_choices_sideurl[0].get_attribute("href")
        
        base_url = "https://www.basketball-reference.com"
        year_official_url = base_url + year_to_select_sideurl

        for indiv_stat_choice in stats_choice_all:
            side_url = indiv_stat_choice.find_element(By.TAG_NAME, "a").get_attribute("href")
            self.driver.get(side_url)
            self.human_behaviour()
            yield HtmlResponse(url=self.driver.current_url, body=self.driver.page_source, encoding='utf-8', request=response)

        self.driver.get(year_official_url)
        self.human_behaviour()
        yield HtmlResponse(url=self.driver.current_url, body=self.driver.page_source, encoding='utf-8', request=response)

    def human_behaviour(self):
        time.sleep(random.uniform(1, 5))
        ActionChains(self.driver).move_by_offset(random.randint(0, 10), random.randint(0, 10)).perform()
        self.driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(random.uniform(1, 5))