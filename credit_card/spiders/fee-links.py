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
    start_urls = ['https://www.hdfcbank.com/personal/pay/cards/credit-cards/moneyback-plus/fees-and-charges',
 'https://www.hdfcbank.comNone/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/indianoil-hdfc-bank-credit-card/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/regalia-gold-credit-card/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/irctc-credit-card/fees-and-charges',
 'https://www.hdfcbank.comNone/fees-and-charges',
 'https://www.hdfcbank.comNone/fees-and-charges',
 'https://www.hdfcbank.comNone/fees-and-charges',
 'https://www.hdfcbank.comNone/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/diners-club-black/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/regalia-gold-credit-card/fees-and-charges',
 'https://www.hdfcbank.comNone/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/moneyback-plus/fees-and-charges',
 'https://www.hdfcbank.comNone/fees-and-charges',
 'https://www.hdfcbank.comNone/fees-and-charges',
 'https://www.hdfcbank.comNone/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/shoppers-stop-hdfc-bank-credit-card/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/shoppers-stop-black-hdfc-bank-credit-card/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/diners-privilege/fees-and-charges',
 'https://www.hdfcbank.comNone/fees-and-charges',
 'https://www.hdfcbank.comNone/fees-and-charges',
 'https://www.hdfcbank.comNone/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/regalia-first/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/diners-club-miles/fees-and-charges',
 'https://www.hdfcbank.comNone/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/regalia/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/platinum-times-credit-card/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/titanium-times-credit-card/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/regalia-gold-credit-card/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/irctc-credit-card/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/6e-rewards-indigo-hdfc-bank-credit-card/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/6e-rewards-xl-indigo-hdfc-bank-credit-card/fees-and-charges',
 'https://www.hdfcbank.comNone/fees-and-charges',
 'https://www.hdfcbank.comNone/fees-and-charges',
 'https://www.hdfcbank.comNone/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/indianoil-hdfc-bank-credit-card/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/millennia-cards/millennia-easyemi-card/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/all-miles-card/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/freedom-card/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/bharat-credit-card/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/commercial-credit-cards/business-bharat-card/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/commercial-credit-cards/business-freedom-card/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/commercial-credit-cards/business-gold/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/commercial-credit-cards/business-platinum/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/commercial-credit-cards/business-regalia-first/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/diners-club-premium/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/diners-club-rewardz/fees-and-charges',
 'https://www.hdfcbank.comNone/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/doctors-superia/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/jetprivilege-hdfc-bank-titanium-credit-card/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/platinum-edge/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/platinum-plus/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/solitaire/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/superia/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/teachers-platinum/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/titanium-edge/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/visa-signature/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/world-mastercard/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/credit-cards/money-back/fees-and-charges',
 'https://www.hdfcbank.com/personal/pay/cards/millennia-cards/millennia-credit-card/fees-and-charges']

def parse(self, response):
        item = Project5Item()
        cardFee = response.xpath("//div[@class='row content-body']//text()[contains(.,'Membership')]").get()
        if not cardFee:
            cardFee= ' '
        item['cardFee'] = cardFee

        yield fee