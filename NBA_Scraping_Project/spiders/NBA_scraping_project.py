import scrapy
from NBA_Scraping_Project.items import TotalsPlayerItem, PlayerPerGameItem, PlayerPer36MinItem, PlayerPer100TeamPossession, AdvancedPlayerStats, PlayerShooting, PlayerAdjustedShooting
import random
import time 

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
    
    # def parse_main_pages(self, response):
    #     main_pages = response.css("")
    

    def parse(self, response): 
        stats_choice_all = response.css("div.filter div")
        # Returns a list of 2 years of links, e.g. 2024 returns 2023 and 2025 links. always return first index
        year_choices_sideurl = response.css("div.prevnext a::attr(href)").getall()
        year_to_select_sideurl = year_choices_sideurl[0]
        base_url = "https://www.basketball-reference.com"
        # To iterate through individual stat choice -- Resolved with results not sorted in order
        for indiv_stat_choice in stats_choice_all: 
            side_url = indiv_stat_choice.css("a ::attr(href)").get()
            # yield indiv_stat_choice.css("a ::attr(href)").get()
            full_url = str(base_url) + str(side_url)
            yield response.follow(full_url, callback=self.parse_stat_page, headers={"User-Agent": random.choice(self.user_agent_list)}, dont_filter=True)
        
        year_official_url = base_url + str(year_to_select_sideurl)
        yield response.follow(year_official_url, callback=self.parse_year, headers={"User-Agent": random.choice(self.user_agent_list)})
        
    def parse_year(self, response): 
        baseurl = "https://www.basketball-reference.com"
        year_choices_sideurl = response.css("div.prevnext a::attr(href)").getall()
        year_to_select_sideurl = year_choices_sideurl[0]
        year_official_url = baseurl + str(year_to_select_sideurl)
        if 
        
    
    def parse_stat_page(self, response):
        table_rows = response.css("table.sortable tbody tr")
        url = response.url

        if "_totals" in url:
            player_details = TotalsPlayerItem()
            # To iterate through individual player row
            for indiv_row in table_rows:
                team_tag = indiv_row.css('td.left[data-stat="team_id"]')
                player_details["ranking"] = indiv_row.css("th ::text").get()
                player_details["name"] = indiv_row.css('td.left ::text').get()
                player_details['position'] = indiv_row.css("td.center ::text").get()
                player_details['age'] = indiv_row.css("td.right ::text").get()
                player_details['team'] = team_tag.css("a ::text").get()
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
                team_tag = each.css('td.left[data-stat="team_id"]')
                player_per_game_details["ranking"] = each.css("th ::text").get()
                player_per_game_details["name"] = each.css('td.left ::text').get()
                player_per_game_details['position'] = each.css("td.center ::text").get()
                player_per_game_details['age'] = each.css("td.right[data-stat='age'] ::text").get()
                player_per_game_details['team'] = team_tag.css("a ::text").get()
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
                team_tag = row.css('td.left[data-stat="team_id"]')
                player_per_min_details["ranking"] = row.css("th::text").get()
                player_per_min_details["name"] = row.css('td.left ::text').get()
                player_per_min_details['position'] = row.css("td.center ::text").get()
                player_per_min_details['age'] = row.css("td.right[data-stat='age'] ::text").get()
                player_per_min_details['team'] = team_tag.css("a ::text").get()
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
                
        elif "_per_poss" in url: 
            player_per_poss_details = PlayerPer100TeamPossession()
            for row in table_rows: 
                team_tag = row.css('td.left[data-stat="team_id"]')
                player_per_poss_details["ranking"] = row.css("th::text").get()
                player_per_poss_details["name"] = row.css('td.left ::text').get()
                player_per_poss_details['position'] = row.css("td.center ::text").get()
                player_per_poss_details['age'] = row.css("td.right[data-stat='age'] ::text").get()
                player_per_poss_details['team'] = team_tag.css("a ::text").get()
                player_per_poss_details['games_played'] = row.css("td.right[data-stat='g'] ::text").get()
                player_per_poss_details['games_started'] = row.css("td.right[data-stat='gs'] ::text").get()
                player_per_poss_details['minutes_played'] = row.css("td.right[data-stat='mp'] ::text").get()
                player_per_poss_details['field_goals_per_100'] = row.css("td.right[data-stat='fg_per_poss'] ::text").get()
                player_per_poss_details['field_goal_attempts_per_100'] = row.css("td.right[data-stat='fga_per_poss'] ::text").get()
                player_per_poss_details['field_goal_percentage'] = row.css("td.right[data-stat='fg_pct'] ::text").get()
                player_per_poss_details['three_pts_made_per_100'] = row.css("td.right[data-stat='fg3_per_poss'] ::text").get()
                player_per_poss_details['three_pts_attempts_per_100'] = row.css("td.right[data-stat='fg3a_per_poss'] ::text").get()
                player_per_poss_details['three_pt_percentage'] = row.css("td.right[data-stat='fg3_pct'] ::text").get()
                player_per_poss_details['two_pts_made_per_100'] = row.css("td.right[data-stat='fg2_per_poss'] ::text").get()
                player_per_poss_details['two_pts_attempts_per_100'] = row.css("td.right[data-stat='fg2a_per_poss'] ::text").get()
                player_per_poss_details['two_pts_percentage'] = row.css("td.right[data-stat='fg2_pct'] ::text").get()
                player_per_poss_details['free_throw_made_per_100'] = row.css("td.right[data-stat='ft_per_poss'] ::text").get()
                player_per_poss_details['free_throw_attempts_per_100'] = row.css("td.right[data-stat='fta_per_poss'] ::text").get()
                player_per_poss_details['free_throw_percentage'] = row.css("td.right[data-stat='ft_pct'] ::text").get()
                player_per_poss_details['offensive_rebound_per_100'] = row.css("td.right[data-stat='orb_per_poss'] ::text").get()
                player_per_poss_details['defensive_rebound_per_100'] = row.css("td.right[data-stat='drb_per_poss'] ::text").get()
                player_per_poss_details['total_rebound_per_100'] = row.css("td.right[data-stat='trb_per_poss'] ::text").get()
                player_per_poss_details['assists_per_100'] = row.css("td.right[data-stat='ast_per_poss'] ::text").get()
                player_per_poss_details['steals_per_100'] = row.css("td.right[data-stat='stl_per_poss'] ::text").get()
                player_per_poss_details['blocks_per_100'] = row.css("td.right[data-stat='blk_per_poss'] ::text").get()
                player_per_poss_details['turnover_per_100'] = row.css("td.right[data-stat='tov_per_poss'] ::text").get()
                player_per_poss_details['personal_fouls_per_100'] = row.css("td.right[data-stat='pf_per_poss'] ::text").get()
                player_per_poss_details['points_per_100'] = row.css("td.right[data-stat='pts_per_poss'] ::text").get()
                player_per_poss_details['offensive_rating'] = row.css("td.right[data-stat='off_rtg'] ::text").get()
                player_per_poss_details['defensive_rating'] = row.css("td.right[data-stat='def_rtg'] ::text").get()
                yield player_per_poss_details
        elif "_advanced" in url:
            player_advanced_details = AdvancedPlayerStats()
            for row in table_rows:
                team_tag = row.css('td.left[data-stat="team_id"]')
                player_advanced_details["ranking"] = row.css("th::text").get()
                player_advanced_details["name"] = row.css('td.left ::text').get()
                player_advanced_details['position'] = row.css("td.center ::text").get()
                player_advanced_details['age'] = row.css("td.right[data-stat='age'] ::text").get()
                player_advanced_details['team'] = team_tag.css("a ::text").get()
                player_advanced_details['games_played'] = row.css("td.right[data-stat='g'] ::text").get()
                player_advanced_details['minutes_played'] = row.css("td.right[data-stat='mp']::text").get()
                player_advanced_details['player_efficiency_rating'] = row.css("td.right[data-stat='per'] ::text").get()
                player_advanced_details['true_shooting_percentage'] = row.css("td.right[data-stat='ts_pct'] ::text").get()
                player_advanced_details['three_pts_attempt_rate'] = row.css("td.right[data-stat='fg3a_per_fga_pct'] ::text").get()
                player_advanced_details['free_throw_attempt_rate'] = row.css("td.right[data-stat='fta_per_fga_pct'] ::text").get()
                player_advanced_details['offensive_rebound_percentage'] = row.css("td.right[data-stat='orb_pct'] ::text").get()
                player_advanced_details['defensive_rebound_percentage'] = row.css("td.right[data-stat='drb_pct'] ::text").get()
                player_advanced_details['total_rebound_percentage'] = row.css("td.right[data-stat='trb_pct'] ::text").get()
                player_advanced_details['assists_percentage'] = row.css("td.right[data-stat='ast_pct'] ::text").get()
                player_advanced_details['steal_percentage'] = row.css("td.right[data-stat='stl_pct'] ::text").get()
                player_advanced_details['block_percentage'] = row.css("td.right[data-stat='blk_pct'] ::text").get()
                player_advanced_details['turnover_percentage'] = row.css("td.right[data-stat='tov_pct'] ::text").get()
                player_advanced_details['usage_percentage'] = row.css("td.right[data-stat='usg_pct'] ::text").get()
                player_advanced_details['offensive_win_shares'] = row.css("td.right[data-stat='ows'] ::text").get()
                player_advanced_details['defensive_win_shares'] = row.css("td.right[data-stat='dws'] ::text").get()
                player_advanced_details['win_shares'] = row.css("td.right[data-stat='ws'] ::text").get()
                player_advanced_details['win_shares_per_48'] = row.css("td.right[data-stat='ws_per_48'] ::text").get()
                player_advanced_details['offensive_box_plus_minus'] = row.css("td.right[data-stat='obpm'] ::text").get()
                player_advanced_details['defensive_box_plus_minus'] = row.css("td.right[data-stat='dbpm'] ::text").get()
                player_advanced_details['box_plus_minus'] = row.css("td.right[data-stat='bpm'] ::text").get()
                player_advanced_details['value_over_replacement_player'] = row.css("td.right[data-stat='vorp'] ::text").get()
                yield player_advanced_details
                
        elif "_shooting" in url: 
            player_shooting_statistics = PlayerShooting() 
            for row in table_rows:
                team_tag = row.css('td.left[data-stat="team_id"]')
                player_shooting_statistics["ranking"] = row.css("th::text").get()
                player_shooting_statistics["name"] = row.css('td.left ::text').get()
                player_shooting_statistics['position'] = row.css("td.center ::text").get()
                player_shooting_statistics['age'] = row.css("td.right[data-stat='age'] ::text").get()
                player_shooting_statistics['team'] = team_tag.css("a ::text").get()
                player_shooting_statistics['games_played'] = row.css("td.right[data-stat='g'] ::text").get()
                player_shooting_statistics['minutes_played'] = row.css("td.right[data-stat='mp']::text").get()
                player_shooting_statistics['field_goal_percentage'] = row.css("td.right[data-stat='fg_pct'] ::text").get()
                player_shooting_statistics['average_distance_field_goal'] = row.css("td.right[data-stat='avg_dist'] ::text").get()
                player_shooting_statistics['percentage_field_goal_attempts_2pts'] = row.css("td.right[data-stat='pct_fga_fg2a'] ::text").get()
                player_shooting_statistics['percentage_field_goal_attempts_0to3ft'] = row.css("td.right[data-stat='pct_fga_00_03'] ::text").get()
                player_shooting_statistics['percentage_field_goal_attempts_3to10ft'] = row.css("td.right[data-stat='pct_fga_03_10'] ::text").get()
                player_shooting_statistics['percentage_field_goal_attempts_10to16ft'] = row.css("td.right[data-stat='pct_fga_10_16'] ::text").get()
                player_shooting_statistics['percentage_field_goal_attempts_16to3pts'] = row.css("td.right[data-stat='pct_fga_16_xx'] ::text").get()
                player_shooting_statistics['percentage_field_goal_attempts_3pts'] = row.css("td.right[data-stat='pct_fga_fg3a'] ::text").get()
                player_shooting_statistics['percentage_fg_made_2pts'] = row.css("td.right[data-stat='fg_pct_fg2a'] ::text").get()
                player_shooting_statistics['percentage_fg_made_0to3ft'] = row.css("td.right[data-stat='fg_pct_00_03'] ::text").get()
                player_shooting_statistics['percentage_fg_made_3to10ft'] = row.css("td.right[data-stat='fg_pct_03_10'] ::text").get()
                player_shooting_statistics['percentage_fg_made_10to16ft'] = row.css("td.right[data-stat='fg_pct_10_16'] ::text").get()
                player_shooting_statistics['percentage_fg_made_16to3pts'] = row.css("td.right[data-stat='fg_pct_16_xx'] ::text").get()
                player_shooting_statistics['percentage_fg_made_3pts'] = row.css("td.right[data-stat='fg_pct_fg3a'] ::text").get()
                player_shooting_statistics['percentage_fg_assists_2pts'] = row.css("td.right[data-stat='pct_ast_fg2'] ::text").get()
                player_shooting_statistics['percentage_fg_assists_3pts'] = row.css("td.right[data-stat='pct_ast_fg3'] ::text").get()
                player_shooting_statistics['percentage_dunks_over_total_fg_attempts'] = row.css("td.right[data-stat='pct_fga_dunk'] ::text").get()
                player_shooting_statistics['number_of_dunks'] = row.css("td.right[data-stat='fg_dunk'] ::text").get()
                player_shooting_statistics['percentage_corner3pts_over_total_3pts_fg_attempts'] = row.css("td.right[data-stat='pct_fg3a_corner3'] ::text").get()
                player_shooting_statistics['percentage_corner3pts_made'] = row.css("td.right[data-stat='fg_pct_corner3'] ::text").get()       
                yield player_shooting_statistics

        # else:
        #     # Could not retrieve adjusted statistics for player at all. Need to figure out. 
        #     # table_rows = response.css("table.row_summable tbody tr")
        #     player_adjusted_shooting_statistics = PlayerAdjustedShooting() 
        #     for row in table_rows:
        #         player_adjusted_shooting_statistics["ranking"] = row.css("th::text").get()
        #         player_adjusted_shooting_statistics["name"] = row.css('td [data-stat="player"] ::text').get()
        #         player_adjusted_shooting_statistics['position'] = row.css("td [data-stat='pos'] ::text").get()
        #         player_adjusted_shooting_statistics['age'] = row.css("td [data-stat='age'] ::text").get()
        #         player_adjusted_shooting_statistics['team'] = row.css("td [data-stat='team_id']::text").get()
        #         player_adjusted_shooting_statistics['games_played'] = row.css("td [data-stat='g'] ::text").get()
        #         player_adjusted_shooting_statistics['minutes_played'] = row.css("td [data-stat='mp']::text").get()
        #         player_adjusted_shooting_statistics['overall_field_goal_percentage'] = row.css("td [data-stat='fg_pct'] ::text").get()
        #         player_adjusted_shooting_statistics['two_pts_field_goal_percentage'] = row.css("td [data-stat='fg2_pct'] ::text").get()
        #         player_adjusted_shooting_statistics['three_pts_field_goal_percentage'] = row.css("td [data-stat='fg3_pct'] ::text").get()
        #         player_adjusted_shooting_statistics['effective_field_goal_percentage'] = row.css("td [data-stat='efg_pct'] ::text").get()
        #         player_adjusted_shooting_statistics['free_throw_percentage'] = row.css("td [data-stat='ft_pct'] ::text").get()
        #         player_adjusted_shooting_statistics['true_shooting_percentage'] = row.css("td [data-stat='ts_pct'] ::text").get()
        #         player_adjusted_shooting_statistics['free_throw_per_field_goal_percentage'] = row.css("td [data-stat='ft_rate'] ::text").get()
        #         player_adjusted_shooting_statistics['league_adjusted_overall_field_goal_percentage'] = row.css("td [data-stat='adj_fg_pct'] ::text").get()
        #         player_adjusted_shooting_statistics['league_adjusted_2pts_field_goal_percentage'] = row.css("td [data-stat='adj_fg2_pct'] ::text").get()
        #         player_adjusted_shooting_statistics['league_adjusted_3pts_field_goal_percentage'] = row.css("td [data-stat='adj_fg3_pct'] ::text").get()
        #         player_adjusted_shooting_statistics['league_adjusted_effective_field_goal_percentage'] = row.css("td [data-stat='adj_efg_pct'] ::text").get()
        #         player_adjusted_shooting_statistics['league_adjusted_free_throw_percentage'] = row.css("td [data-stat='adj_ft_pct'] ::text").get()
        #         player_adjusted_shooting_statistics['league_adjusted_true_shooting_percentage'] = row.css("td [data-stat='adj_ts_pct'] ::text").get()
        #         player_adjusted_shooting_statistics['league_adjusted_free_throw_per_field_goal_percentage'] = row.css("td [data-stat='adj_ft_rate'] ::text").get()
        #         player_adjusted_shooting_statistics['extra_pts_by_FGA_above_league_average'] = row.css("td [data-stat='fg_pts_added'] ::text").get()
        #         player_adjusted_shooting_statistics['extra_pts_by_TrueShotAttempts_above_league_average'] = row.css("td [data-stat='ts_pts_added'] ::text").get()
        #         yield player_adjusted_shooting_statistics
                

def handle_error(self, failure):
    # Error handling logic here
    if failure.check(TimeoutError):
        self.logger.error('Request timed out.')
        yield scrapy.Request(callback=self.parse, errback=self.handle_error,headers={"User-Agent": random.choice(self.user_agent_list)})