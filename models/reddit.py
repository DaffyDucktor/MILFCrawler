# reddit.py

from scrapy.item import Item, Field


class CreepypastaItem(Item):
    title = Field()
    autor = Field()
    text = Field()
    subreddit = Field()
    upvote = Field()
