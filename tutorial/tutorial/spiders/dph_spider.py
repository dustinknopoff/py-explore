import scrapy


class DPHSpider(scrapy.Spider):
    name = "daphne"
    start_urls = [
        'https://www.fanfiction.net/book/Harry-Potter/?&srt=4&lan=1&r=10&c1=5549&c2=1',
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
