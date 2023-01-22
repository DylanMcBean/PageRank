import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urljoin, urlparse
import re


def split_url(url):
    return [{"protocol": x[0], "host_domain": x[1], "domain_name": x[2]}
            for x in re.findall(r"(https?:\/\/)([^.]*\.)?([\w\d\-]+(?:\.\w+)+)", url)][0]


class MySpider(CrawlSpider):

    name = "ranker"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]
    rules = (
        # Extract and follow all links, Except those with query parameters
        Rule(LinkExtractor(deny=".*\\?.*"), callback='parse_item', follow=True),
    )

    def __init__(self, url, *args, **kwargs):
        url_data = split_url(url)
        super().__init__(*args, **kwargs)
        if url_data["domain_name"]:
            self.name = url_data["domain_name"]
            self.allowed_domains = [url_data["domain_name"]]
            self.start_urls = [
                f"{url_data['protocol']}{url_data['host_domain']}{url_data['domain_name']}"]
        else:
            self.name = "ranker"
            self.allowed_domains = ["example.com"]
            self.start_urls = ["https://example.com"]
        print(f"Gathering Pages for '{url_data['domain_name']}'")

    def clean_link(self, url):
        parsed = urlparse(url)
        if parsed.path[-1] != "/":
            return f"{parsed.scheme}://{parsed.netloc}{parsed.path}/"
        else:
            return f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

    def parse_item(self, response):
        page_links = response.css('a::attr(href)')
        print(f"Crawled: {response.url}, Links: {len(page_links)}")
        yield {
            "url": self.clean_link(response.url),
            "links": [self.clean_link(urljoin(response.url, link.get())) for link in page_links]
        }
