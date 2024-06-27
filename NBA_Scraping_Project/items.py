# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NbaScrapingProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class TotalsPlayerItem(scrapy.Item): 
    ranking = scrapy.Field()
    name = scrapy.Field()
    position = scrapy.Field()
    age = scrapy.Field()
    team = scrapy.Field()
    games_played = scrapy.Field()
    games_started = scrapy.Field()
    minutes_played = scrapy.Field()
    field_goal_made = scrapy.Field()
    field_goal_attempts = scrapy.Field()
    field_goal_percentage = scrapy.Field()
    three_pts_made = scrapy.Field()
    three_pts_attempts = scrapy.Field()
    three_pt_percentage = scrapy.Field()
    two_pts_made = scrapy.Field()
    two_pts_attempts = scrapy.Field()
    two_pts_percentage = scrapy.Field()
    effective_field_goal_percentage = scrapy.Field()
    free_throw_made = scrapy.Field()
    free_throw_attempts = scrapy.Field()
    free_throw_percentage = scrapy.Field()
    offensive_rebound = scrapy.Field()
    defensive_rebound = scrapy.Field()
    total_rebound = scrapy.Field()
    assists = scrapy.Field()
    turnover = scrapy.Field()
    steals = scrapy.Field()
    blocks = scrapy.Field()
    personal_fouls = scrapy.Field()
    points = scrapy.Field()
    
    

class PlayerPerGameItem(scrapy.Item):
    ranking = scrapy.Field()
    name = scrapy.Field()
    position = scrapy.Field()
    age = scrapy.Field()
    team = scrapy.Field()
    games_played = scrapy.Field()
    games_started = scrapy.Field()
    minutes_played_pg = scrapy.Field()
    field_goal_made_pg = scrapy.Field()
    field_goal_attempts_pg = scrapy.Field()
    field_goal_percentage = scrapy.Field()
    three_pts_made_pg = scrapy.Field()
    three_pts_attempts_pg = scrapy.Field()
    three_pt_percentage = scrapy.Field()
    two_pts_made_pg = scrapy.Field()
    two_pts_attempts_pg = scrapy.Field()
    two_pts_percentage = scrapy.Field()
    effective_field_goal_percentage = scrapy.Field()
    free_throw_made_pg = scrapy.Field()
    free_throw_attempts_pg = scrapy.Field()
    free_throw_percentage = scrapy.Field()
    offensive_rebound_pg = scrapy.Field()
    defensive_rebound_pg = scrapy.Field()
    total_rebound_pg = scrapy.Field()
    assists_pg = scrapy.Field()
    turnover_pg = scrapy.Field()
    steals_pg = scrapy.Field()
    blocks_pg = scrapy.Field()
    personal_fouls_pg = scrapy.Field()
    points_pg = scrapy.Field()
    

class PlayerPer36MinItem(scrapy.Item): 
    ranking = scrapy.Field()
    name = scrapy.Field()
    position = scrapy.Field()
    age = scrapy.Field()
    team = scrapy.Field()
    minutes_played = scrapy.Field()
    field_goal_made_36 = scrapy.Field()
    field_goal_attempts_36 = scrapy.Field()
    field_goal_percentage = scrapy.Field()
    three_pts_made_36 = scrapy.Field()
    three_pts_attempts_36 = scrapy.Field()
    three_pt_percentage = scrapy.Field()
    two_pts_made_36 = scrapy.Field()
    two_pts_attempts_36 = scrapy.Field()
    two_pts_percentage = scrapy.Field()
    free_throw_made_36 = scrapy.Field()
    free_throw_attempts_36 = scrapy.Field()
    free_throw_percentage = scrapy.Field()
    offensive_rebound_36 = scrapy.Field()
    defensive_rebound_36 = scrapy.Field()
    total_rebound_36 = scrapy.Field()
    assists_36 = scrapy.Field()
    turnover_36 = scrapy.Field()
    steals_36 = scrapy.Field()
    blocks_36 = scrapy.Field()
    personal_fouls_36 = scrapy.Field()
    points_36 = scrapy.Field()
    
    
    
    
    
    
    
