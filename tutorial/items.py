# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose

def remove_quotes(text):
    text = text.strip(u'\u201c'u'\u201d')
    return text

class QuoteItem(Item):
    quote_content = Field()
    tags = Field()
    author_name = Field()
    author_birthday = Field()
    author_bornlocation = Field()
    author_bio = Field()

# class TutorialItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass
