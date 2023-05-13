BOT_NAME = 'credit_card'

SPIDER_MODULES = ['credit_card.spiders']
NEWSPIDER_MODULE = 'credit_card.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
