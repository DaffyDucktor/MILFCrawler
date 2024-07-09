from pathlib import Path

import scrapy


class CreepypastacrawlerSpider(scrapy.Spider):
    name = "creepypastaCrawler"
    allowed_domains = ["creepypasta.com"]
    start_urls = ["https://www.creepypasta.com/archive/top-ranked/"]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"creepypasta-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
