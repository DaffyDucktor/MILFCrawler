# creepypasta.py

from scrapy.item import Item, Field


class CreepypastaItem(Item):
    title = Field()
    tags = Field()
    rating = Field()
    time = Field()
    text = Field()
