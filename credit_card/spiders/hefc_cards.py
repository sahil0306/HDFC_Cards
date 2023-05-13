import scrapy
import pdb
from scrapy.selector import Selector
import requests
import json
import itertools
from scrapy import Request
import re
from credit_card.items import CreditcardItem


class HefcCardsSpider(scrapy.Spider):
    name = 'hefc-cards'
    start_urls = ["https://www.hdfcbank.com/personal/pay/cards/credit-cards"]

    def parse(self, response):
        item = CreditcardItem()
        blocks = response.xpath("//div[@class='cardWrapper clearfix']//div[@class='card-offer-contr']")
        for block in blocks:
            cardName = block.xpath(".//h2[@class='cardTitle']//span[@class='card-name']//text()").get()
            know_more_link = block.xpath(".//div[@class='row bodyArea']//a[@title='Card Image']//@href").get()
            if not know_more_link:
                know_more_link = block.xpath(".//div[@class='row bodyArea']//a[@title='KNOW MORE']//@href | .//div[@class='row bodyArea']//a[@title='Know More']//@href |.//div[@class='btnParent']//a[@class='btn  btn-custom btn-default-custom btn-default know-more-btn normal-url']//@href").get()
            link = f"https://www.hdfcbank.com{know_more_link}/fees-and-charges"
            fee_response = Selector(text=requests.get(link).text)
            cardFee = fee_response.xpath("//div[@class='row content-body']//text()[contains(.,'Membership')]").get()
            if not cardFee:
                cardFee = ' '
            new_link = f"https://www.hdfcbank.com{know_more_link}"
            new_response =Selector(text=requests.get(new_link).text)
            rewardPoints = " | ".join([i.strip() for i in new_response.xpath("//div[@class='accordion']//div[@class='inner-content col-lg-8 col-sm-8 right-section'][preceding-sibling::div[@class='inner-content col-lg-4 col-sm-4 left-section'][contains(.,'Reward')]]//ul//li//text()").getall() if i.strip()])
            loungeAccess = " | ".join([i.strip() for i in new_response.xpath("//div[@class='accordion']//div[@class='inner-content col-lg-8 col-sm-8 right-section'][preceding-sibling::div[@class='inner-content col-lg-4 col-sm-4 left-section'][contains(.,'Lounge')]]//p//text()").getall() if i.strip()])
            milestoneBenefit = " | ".join([i.strip() for i in new_response.xpath("//div[@class='accordion']//div[@class='inner-content col-lg-8 col-sm-8 right-section'][preceding-sibling::div[@class='inner-content col-lg-4 col-sm-4 left-section'][contains(.,'Key Features')]]//ul//li//text()").getall() if i.strip()])
            
            item['cardName'] = cardName
            item['cardFeeLink'] = link
            item['cardFee'] = cardFee
            item['rewardPoints'] = rewardPoints
            item['milestoneBenefit'] = milestoneBenefit
            item['loungeAccess'] = loungeAccess
            yield item
