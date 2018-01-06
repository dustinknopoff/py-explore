import scrapy


class RGSpider(scrapy.Spider):
    name = "rias"
    start_urls = [
        'https://www.fanfiction.net/Naruto-and-High-School-DxD-ハイスクールD-D-Crossovers/1402/9502/?&srt=4&lan=1&r=10&c3=80170',
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
