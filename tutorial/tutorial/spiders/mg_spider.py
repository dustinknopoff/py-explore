import scrapy


class MGSpider(scrapy.Spider):
    name = "morgana"
    start_urls = [
        'https://www.fanfiction.net/tv/Merlin/?&srt=4&lan=1&r=10&c1=15347&c2=15346',
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
        next_page = response.xpath('//center/a[contains(text(), "Next")]/@href').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
