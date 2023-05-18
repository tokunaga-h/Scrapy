import scrapy
import sys
import unicodedata
from jleague.items import JleagueItem

class CompetitionSpider(scrapy.Spider):
    name = "competition"
    allowed_domains = ["data.j-league.or.jp"]

    def __init__(self, season='', *args, **kwargs):
        super(CompetitionSpider, self).__init__(*args, **kwargs)
        self.start_urls = ["https://data.j-league.or.jp/SFMS01/search?competition_years=" + season ]

    def parse(self, response):
            results = response.css('.search-table tbody tr')

            if not results:
                sys.stdout.write("No results found\n")
                return
            
            for result in results:
                season = result.xpath('td[1]/text()').get()
                # score分割
                try:
                    scores = result.xpath('td[7]/a/text()').get().split('-')
                    home_score = scores[0]
                    away_score = scores[1]
                except:
                    home_score = None
                    away_score = None
                    pass
                # visitors整形
                visitors = result.xpath('td[10]/text()').get().replace('\r\n', '').replace('\t', '').replace(',', '').replace(u'\xa0', u'')
                if visitors == '':
                    visitors = None

                yield JleagueItem (
                    season =  season,
                    competition =  result.xpath('td[2]/text()').get(),
                    matchweek =  result.xpath('td[3]/text()').get(),
                    # yyyy-mm-ddに変換
                    date =  season + '-' + result.xpath('td[4]/text()').get().split('(')[0].replace('/', '-'),
                    home_team =  result.xpath('td[6]/a/text()').get(),
                    home_score =  home_score,
                    away_team =  result.xpath('td[8]/a/text()').get(),
                    away_score =  away_score,
                    stadium =  result.xpath('td[9]/text()').get().replace('\r\n', '').replace('\t', ''),
                    visitors =  visitors,
                    tv =  result.xpath('td[11]/text()').get()
                )
