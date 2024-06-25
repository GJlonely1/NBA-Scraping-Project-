import scrapy
from NBA_Scraping_Project.items import PlayerItem
import random
import time 
# from scrapy_splash import SplashRequest

class NbaScrapingProjectSpider(scrapy.Spider):
    name = "NBA_scraping_project"
    allowed_domains = ["www.nba.com"]
    start_urls = ["https://www.basketball-reference.com/leagues/NBA_2024_totals.html"]
    # start_urls = ["https://www.nba.com/stats/players/traditional?PerMode=Totals"]
    download_timeout = 500

    user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
    ]
    
    def start_requests(self, response):
        for url in self.start_urls: 
            yield response.follow(url, self.parse_player_row, args={'wait' : 2})

    def parse_player_row(self, response):
        table_rows = response.css("table.sortable tbody tr")
        player_details = PlayerItem()
        
        for indiv_row in table_rows:
            player_details["ranking"] = indiv_row.css("th ::text").get()
            player_details["name"] = indiv_row.css('td.left ::text').get()
            player_details['position'] = indiv_row.css("td.center ::text").get()
            player_details['age'] = indiv_row.css("td.right ::text").get()
            player_details['team'] = indiv_row.css('td.left[data-stat="team_id"]::text').get()
            player_details['games_played'] = indiv_row.css('td.right[data-stat="g"]::text').get()
            player_details['games_started'] = indiv_row.css('td.right[data-stat="gs"]::text').get()
            player_details['minutes_played'] = indiv_row.css('td.right[data-stat="mp"]::text').get()
            player_details['field_goal_made'] = indiv_row.css('td.right[data-stat="fg"]::text').get()
            player_details['field_goal_attempts'] = indiv_row.css('td.right[data-stat="fga"]::text').get()
            player_details['field_goal_percentage'] = indiv_row.css('td.right[data-stat="fg_pct"]::text').get()
            player_details['three_pts_made'] = indiv_row.css('td.right[data-stat="fg3"]::text').get()
            player_details['three_pts_attempts'] = indiv_row.css('td.right[data-stat="fg3a"]::text').get()
            player_details['three_pt_percentage'] = indiv_row.css('td.right[data-stat="fg3_pct"]::text').get()
            player_details['two_pts_made'] = indiv_row.css('td.right[data-stat="fg2"]::text').get()
            player_details['two_pts_attempts'] = indiv_row.css('td.right[data-stat="fg2a"]::text').get()
            player_details['two_pts_percentage'] = indiv_row.css('td.right[data-stat="fg2_pct"]::text').get()
            player_details['effective_field_goal_percentage'] = indiv_row.css('td.right[data-stat="efg_pct"]::text').get()
            player_details['free_throw_made'] = indiv_row.css('td.right[data-stat="ft"]::text').get()
            player_details['free_throw_attempts'] = indiv_row.css('td.right[data-stat="fta"]::text').get()
            player_details['free_throw_percentage'] = indiv_row.css('td.right[data-stat="ft_pct"]::text').get()
            player_details['offensive_rebound'] = indiv_row.css('td.right[data-stat="orb"]::text').get()
            player_details['defensive_rebound'] = indiv_row.css('td.right[data-stat="drb"]::text').get()
            player_details['total_rebound'] = indiv_row.css('td.right[data-stat="trb"]::text').get()
            player_details['assists'] = indiv_row.css('td.right[data-stat="ast"]::text').get()
            player_details['turnover'] = indiv_row.css('td.right[data-stat="tov"]::text').get()
            player_details['steals'] = indiv_row.css('td.right[data-stat="stl"]::text').get()
            player_details['blocks'] = indiv_row.css('td.right[data-stat="blk"]::text').get()
            player_details['personal_fouls'] = indiv_row.css('td.right[data-stat="pf"]::text').get()
            player_details['points'] = indiv_row.css('td.right[data-stat="pts"]::text').get()
    
            yield player_details    

        
        # yield response.follow(callback=self.parse_player_row,headers = {"User-Agent": self.user_agent_list[random.randint(0, len(self.user_agent_list) - 1)]})


def handle_error(self, failure):
    # Error handling logic here
    if failure.check(TimeoutError):
        self.logger.error('Request timed out.')

    # yield scrapy.Request(url, callback=self.parse, errback=self.handle_error)