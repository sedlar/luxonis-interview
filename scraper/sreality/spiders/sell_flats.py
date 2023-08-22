import scrapy
from sreality.items import Flat


NUMBER_OF_PAGES_TO_SCRAPE = 10
PAGE_SIZE = 50


class QuotesSpider(scrapy.Spider):
    name = "flats"
    start_urls = [
        f"https://www.sreality.cz/api/cs/v2/estates" \
        f"?category_main_cb=1&category_type_cb=1&page={page}&per_page={PAGE_SIZE}"
        for page in range(1, NUMBER_OF_PAGES_TO_SCRAPE + 1)
    ]

    def parse(self, response, **kwargs):
        response_json = response.json()
        for estate in response_json["_embedded"]["estates"]:
            yield Flat(title=estate["name"], image_url=estate["_links"]["images"][0]["href"])
