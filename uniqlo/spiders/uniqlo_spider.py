import scrapy
from uniqlo.items import ClothItem


class UniqloSpider(scrapy.Spider):
    name = 'uniqlo'
    allowed_domains = ['uniqlo.com']
    start_urls = [
                "http://www.uniqlo.com/sg/",
            ]
    group_id = 0

    def parse(self, response):
        for url in response.xpath('//div[@class="cateNaviLink"]/a/@href').extract():
            yield  scrapy.Request(url, callback=self.parse_category)

    def parse_category(self, response):
        # Find all the collection page
        for item in response.xpath('//ul[contains(@class, "products-grid")]/li/a/@href').extract():
            yield scrapy.Request(item, callback=self.parse_item)

    def parse_item(self, response):
        # Takes the cloth detail url, and extract information form the page
        cols = response.xpath('//ul[@id="listChipColor"]/li/a')
        images = response.xpath('//ul[@id="listChipColor"]/li/a/img/@largesrc').extract()
        title = response.xpath('//h1[@id="goodsNmArea"]/span/text()').extract()
        description = response.xpath('//div[@id="prodDetail"]/div[contains(@class, "content")]/text()').extract()[1].strip()
        code = response.xpath('//ul[@class="basic"]/li[@class="number"]/text()').extract()
        item_code  = code[0].split()[-1]
        price = response.xpath('//div[@class="price-box"]/p/span[@id="product-price-7"]/text()').extract()
        path = path = response.xpath('//p[@class="pathdetail"]/a/text()').extract()
        trace = '/'.join(path)
        size = response.xpath('//ul[@id="listChipSize"]/li/a/@title').extract()
        self.group_id  += 1

        for col in cols:
            color =  col.xpath('@title').extract()
            image = col.xpath('img/@largesrc').extract()
            item = ClothItem(title=title, description=description,price=price,
                    item_code=item_code, trace=trace, image=image,
                    detail_image=images, color=color, group_id=self.group_id, size=size)
            print(item)
            print("NEXT  ITEM !!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("Next Group ======================================")
