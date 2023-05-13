# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CreditcardPipeline:
    def process_item(self, item, spider):
        return item
