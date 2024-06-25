# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NbaScrapingProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class PlayerItem(scrapy.Item): 
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
    
    
    
