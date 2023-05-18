# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JleagueItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    season = scrapy.Field()
    competition = scrapy.Field()
    matchweek = scrapy.Field()
    date = scrapy.Field()
    home_team = scrapy.Field()
    home_score = scrapy.Field()
    away_team = scrapy.Field()
    away_score = scrapy.Field()
    stadium = scrapy.Field()
    visitors = scrapy.Field()
    tv = scrapy.Field()
    pass
