# Define here the models for scraped items

import scrapy

class CreditcardItem(scrapy.Item):
    # define the fields for your item here like:
    cardName = scrapy.Field()
    cardFeeLink = scrapy.Field()
    cardFee = scrapy.Field()
    rewardPoints = scrapy.Field()
    loungeAccess = scrapy.Field()
    milestoneBenefit = scrapy.Field()
