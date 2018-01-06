import scrapy


class FlUSpider(scrapy.Spider):
    name = "fleuru"
    start_urls = [
        'https://www.fanfiction.net/book/Harry-Potter/?&srt=1&lan=1&r=10&c1=349&c2=1',
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
