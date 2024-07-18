from pathlib import Path

import scrapy


class CreepypastacrawlerSpider(scrapy.Spider):
    name = "creepypastaCrawler"
    allowed_domains = ["creepypasta.com"]
    start_urls = ["https://www.creepypasta.com/archive/top-ranked/"]

    def parse(self, response):
        stories = response.css('div.pt-cv-ifield')
        for story in stories:
            if story.css('a.cvplbd::text').get() is not None:
                yield{
                    'name' : story.css('a.cvplbd::text').get(),
                    'rating': story.css('div.pt-cv-ctf-value::text').get(),
                    'date': story.css('time::text').get(),
                    'description': story.css('div.pt-cv-content::text').get(),
                    'link': story.css('a.cvplbd').attrib['href'],
                }
