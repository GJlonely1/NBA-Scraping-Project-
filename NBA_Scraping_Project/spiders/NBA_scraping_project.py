import scrapy
from NBA_Scraping_Project.items import TotalsPlayerItem, PlayerPerGameItem, PlayerPer36MinItem
import random
import time 
# from scrapy_splash import SplashRequest

class NbaScrapingProjectSpider(scrapy.Spider):
    name = "NBA_scraping_project"
    allowed_domains = ["NBA_2024_per_game.html", "NBA_2024_per_minute.html", "NBA_2024_per_poss.html", "NBA_2024_advanced.html", "NBA_2024_play-by-play.html", "NBA_2024_shooting.html", "NBA_2024_adj_shooting.html"]
    start_urls = ["https://www.basketball-reference.com/leagues/NBA_2024_totals.html"]
    # start_urls = ["https://www.nba.com/stats/players/traditional?PerMode=Totals"]
    # download_timeout = 500

    user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
    ]
    
    # def start_requests(self):
    #     for url in self.start_urls: 
    #         yield scrapy.Request(url, calback=self.parse, headers={"User-Agent": random.choice(self.user_agent_list)})

    def parse(self, response): 
        stats_choice_all = response.css("div.filter div")
        base_url = "https://www.basketball-reference.com"
        # To iterate through individual stat choice -- Resolved with results not sorted in order
        for indiv_stat_choice in stats_choice_all: 
            side_url = indiv_stat_choice.css("a ::attr(href)").get()
            # yield indiv_stat_choice.css("a ::attr(href)").get()
            full_url = str(base_url) + str(side_url)
            yield response.follow(full_url, callback=self.parse_stat_page, headers={"User-Agent": random.choice(self.user_agent_list)}, dont_filter=True)
    
    def parse_stat_page(self, response):
        table_rows = response.css("table.sortable tbody tr")
        url = response.url

        if "_totals" in url:
            player_details = TotalsPlayerItem()
            # To iterate through individual player row
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
            
        elif "_per_game" in url: 
            player_per_game_details = PlayerPerGameItem()
            for each in table_rows: 
                player_per_game_details["ranking"] = each.css("th ::text").get()
                player_per_game_details["name"] = each.css('td.left ::text').get()
                player_per_game_details['position'] = each.css("td.center ::text").get()
                player_per_game_details['age'] = each.css("td.right[data-stat='age'] ::text").get()
                player_per_game_details['team'] = each.css('td.left[data-stat="team_id"]::text').get()
                player_per_game_details['games_played'] = each.css('td.right[data-stat="g"]::text').get()
                player_per_game_details['games_started'] = each.css('td.right[data-stat="gs"]::text').get()
                player_per_game_details['minutes_played_pg'] = each.css('td.right[data-stat="mp_per_g"]::text').get()
                player_per_game_details['field_goal_made_pg'] = each.css('td.right[data-stat="fg_per_g"]::text').get()
                player_per_game_details['field_goal_attempts_pg'] = each.css('td.right[data-stat="fga_per_g"]::text').get()
                player_per_game_details['field_goal_percentage'] = each.css('td.right[data-stat="fg_pct"]::text').get()
                player_per_game_details['three_pts_made_pg'] = each.css('td.right[data-stat="fg3_per_g"]::text').get()      
                player_per_game_details['three_pts_attempts_pg'] = each.css('td.right[data-stat="fg3a_per_g"]::text').get()
                player_per_game_details['three_pt_percentage'] = each.css('td.right[data-stat="fg3_pct"]::text').get()
                player_per_game_details['two_pts_made_pg'] = each.css('td.right[data-stat="fg2_per_g"]::text').get()
                player_per_game_details['two_pts_attempts_pg'] = each.css('td.right[data-stat="fg2a_per_g"]::text').get()
                player_per_game_details['two_pts_percentage'] = each.css('td.right[data-stat="fg2_pct"]::text').get()
                player_per_game_details['effective_field_goal_percentage'] = each.css('td.right[data-stat="efg_pct"]::text').get()
                player_per_game_details['free_throw_made_pg'] = each.css('td.right[data-stat="ft_per_g"]::text').get()
                player_per_game_details['free_throw_attempts_pg'] = each.css('td.right[data-stat="fta_per_g"]::text').get()
                player_per_game_details['free_throw_percentage'] = each.css('td.right[data-stat="ft_pct"]::text').get()
                player_per_game_details['offensive_rebound_pg'] = each.css('td.right[data-stat="orb_per_g"]::text').get()                 
                player_per_game_details['defensive_rebound_pg'] = each.css('td.right[data-stat="drb_per_g"]::text').get()
                player_per_game_details['total_rebound_pg'] = each.css('td.right[data-stat="trb_per_g"]::text').get()
                player_per_game_details['assists_pg'] = each.css('td.right[data-stat="ast_per_g"]::text').get()
                player_per_game_details['turnover_pg'] = each.css('td.right[data-stat="tov_per_g"]::text').get()
                player_per_game_details['steals_pg'] = each.css('td.right[data-stat="stl_per_g"]::text').get()
                player_per_game_details['blocks_pg'] = each.css('td.right[data-stat="blk_per_g"]::text').get()
                player_per_game_details['personal_fouls_pg'] = each.css('td.right[data-stat="pf_per_g"]::text').get()
                player_per_game_details['points_pg'] = each.css('td.right[data-stat="pts_per_g"]::text').get()
                yield player_per_game_details
            
        elif "_per_minute" in url:  
            player_per_min_details = PlayerPer36MinItem()
            for row in table_rows: 
                player_per_min_details["ranking"] = row.css("th::text").get()
                player_per_min_details["name"] = row.css('td.left ::text').get()
                player_per_min_details['position'] = row.css("td.center ::text").get()
                player_per_min_details['age'] = row.css("td.right[data-stat='age'] ::text").get()
                player_per_min_details['team'] = row.css("td.left[data-stat='team_id']::text").get()
                player_per_min_details['games_played'] = row.css("td.right[data-stat='g'] ::text").get()
                player_per_min_details['games_started'] = row.css("td.right[data-stat='gs'] ::text").get()
                player_per_min_details['minutes_played'] = row.css("td.right[data-stat='mp'] ::text").get()
                player_per_min_details['field_goal_made_36'] = row.css("td.right[data-stat='fg_per_mp'] ::text").get()
                player_per_min_details['field_goal_attempts_36'] = row.css("td.right[data-stat='fga_per_mp'] ::text").get()
                player_per_min_details['field_goal_percentage'] = row.css("td.right[data-stat='fg_pct'] ::text").get()
                player_per_min_details['three_pts_made_36'] = row.css("td.right[data-stat='fg3_per_mp'] ::text").get()
                player_per_min_details['three_pts_attempts_36'] = row.css("td.right[data-stat='fg3a_per_mp'] ::text").get()
                player_per_min_details['three_pt_percentage'] = row.css("td.right[data-stat='fg3_pct'] ::text").get()
                player_per_min_details['two_pts_made_36'] = row.css("td.right[data-stat='fg2_per_mp'] ::text").get()
                player_per_min_details['two_pts_attempts_36'] = row.css("td.right[data-stat='fg2a_per_mp'] ::text").get()
                player_per_min_details['two_pts_percentage'] = row.css("td.right[data-stat='fg2_pct'] ::text").get()
                player_per_min_details['free_throw_made_36'] = row.css("td.right[data-stat='ft_per_mp'] ::text").get()
                player_per_min_details['free_throw_attempts_36'] = row.css("td.right[data-stat='fta_per_mp'] ::text").get()
                player_per_min_details['free_throw_percentage'] = row.css("td.right[data-stat='ft_pct'] ::text").get()
                player_per_min_details['offensive_rebound_36'] = row.css("td.right[data-stat='orb_per_mp'] ::text").get()
                player_per_min_details['defensive_rebound_36'] = row.css("td.right[data-stat='drb_per_mp'] ::text").get()
                player_per_min_details['total_rebound_36'] = row.css("td.right[data-stat='trb_per_mp'] ::text").get()
                player_per_min_details['assists_36'] = row.css("td.right[data-stat='ast_per_mp'] ::text").get()
                player_per_min_details['turnover_36'] = row.css("td.right[data-stat='tov_per_mp'] ::text").get()
                player_per_min_details['steals_36'] = row.css("td.right[data-stat='stl_per_mp'] ::text").get()
                player_per_min_details['blocks_36'] = row.css("td.right[data-stat='blk_per_mp'] ::text").get()
                player_per_min_details['personal_fouls_36'] = row.css("td.right[data-stat='pf_per_mp'] ::text").get()
                player_per_min_details['points_36'] = row.css("td.right[data-stat='pts_per_mp'] ::text").get()
                yield player_per_min_details
               
            # yield response.follow(callback=self.parse, headers={"User-Agent": random.choice(self.user_agent_list)})

def handle_error(self, failure):
    # Error handling logic here
    if failure.check(TimeoutError):
        self.logger.error('Request timed out.')
        yield scrapy.Request(callback=self.parse, errback=self.handle_error,headers={"User-Agent": random.choice(self.user_agent_list)})