import scrapy


class MarathonSpider(scrapy.Spider):
    name = "marathon2019"
    start_urls = [
        'https://www.almaty-marathon.kz/en/results/almaty_marafon_2019?ajax=data-grid&Results_page=1',
    ]

    def parse(self, response):
        for marathon in response.css('tbody tr'):
            yield {
                'place': marathon.css('td.auto::text').get(),
                'participant': marathon.css('td.fio a::text').get(),
                'city': marathon.css('td.city::text').get(),
                'bib': marathon.css('td.start_id::text').get(),
                'finish_time': marathon.css('td.ft::text').get(),
                'chip_time': marathon.css('td.ct::text').get(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
