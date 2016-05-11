import scrapy
from uniqlo.items import ClothItem
import hashlib
import os


class UniqloSpider(scrapy.Spider):
    name = 'uniqlo'
    allowed_domains = ['uniqlo.com']
    start_urls = [
                "http://www.uniqlo.com/sg/",
            ]
    group_id = 0
    CWD = os.getcwd()

    def parse(self, response):
        for url in response.xpath('//div[@class="cateNaviLink"]/a/@href').extract():
            yield  scrapy.Request(url, callback=self.parse_category)

    def parse_category(self, response):
        # Find all the collection page
        for item in response.xpath('//ul[contains(@class, "products-grid")]/li/a/@href').extract():
            yield scrapy.Request(item, callback=self.parse_item)

    
    def list_to_str(self, target):
        return ','.join([str(i) for i in target])

    def parse_item(self, response):
        # Takes the cloth detail url, and extract information form the page
        cols = response.xpath('//ul[@id="listChipColor"]/li/a')
        image_list_urls = response.xpath('//ul[@id="listChipColor"]/li/a/img/@largesrc').extract()

        image_list_urls = [hashlib.md5('http:' + i).hexdigest() for i in image_list_urls]
        image_list_urls = [self.CWD + '/full/' + i + 'jpg' for i in image_list_urls ]
        
        title = response.xpath('//h1[@id="goodsNmArea"]/span/text()').extract()[0]
        description = response.xpath('//div[@id="prodDetail"]/div[contains(@class, "content")]/text()').extract()[1].strip()
        code = response.xpath('//ul[@class="basic"]/li[@class="number"]/text()').extract()
        item_code  = code[0].split()[-1]
        price = response.xpath('//div[@class="price-box"]/p/span[@id="product-price-7"]/text()').re('(\d+.\d+)')[0]
        path =  response.xpath('//p[@class="pathdetail"]/a/text()').extract()
        category = title.split()[0]
        path = '/'.join(path)
        trace = category + '/' + path
        size = response.xpath('//ul[@id="listChipSize"]/li/a/@title').extract()
        size = self.list_to_str(size)
        self.group_id  += 1

        for col in cols:
            color =  col.xpath('@title').extract()[0]
            image_urls = col.xpath('img/@largesrc').extract()[0]
            image_urls = 'http:' + image_urls
            image_path = self.CWD + '/full/' + hashlib.md5(image_urls).hexdigest()+'.jpg'
            item = ClothItem(title=title, description=description,price=price,
                    item_code=item_code, trace=trace, image_urls=[image_urls], image_path=image_path, color=color, group_id=self.group_id, image_list_path=image_list_urls, size=size)
            yield item
