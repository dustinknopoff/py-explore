import scrapy


class FavsSpider(scrapy.Spider):
    name = "favorites"
    start_urls = [
        'https://www.fanfiction.net/u/7423303/',
    ]

    def parse(self, response):
        for fav in response.css('div.z-list'):
            yield {
                'title': fav.css('a.stitle::text').extract_first(),
                'link': fav.css('a.stitle::attr(href)').extract_first(),
                'img': fav.css('img.lazy::attr(src)').extract_first(),
                'summary': fav.css('div.z-indent::text').extract(),
                'info': fav.css('div.z-padtop2::text').extract(),
                'reviews': fav.xpath('//a[@class="reviews"]/@href').extract_first(),
            }
