import scrapy


class SWUSpider(scrapy.Spider):
    name = "dianau"
    start_urls = [
        'https://www.fanfiction.net/community/Superman-Wonder-Woman-FanFics/92746/99/1/1/0/0/0/0/',
    ]

    def parse(self, response):
        for story in response.css('div.z-list'):
            yield {
                'title': story.css('a.stitle::text').extract_first(),
                'link': story.css('a.stitle::attr(href)').extract_first(),
                'img': story.css('img.lazy::attr(src)').extract_first(),
                'summary': story.css('div.z-indent::text').extract(),
                'info': story.css('div.z-padtop2::text').extract(),
                'reviews': story.xpath('//a[@class="reviews"]/@href').extract_first(),
            }
