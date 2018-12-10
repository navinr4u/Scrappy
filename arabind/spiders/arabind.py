import scrapy

class AraBind(scrapy.Spider):
	name = 'arabind'
	start_urls = ['http://arabind.com/arabind/home/home.action?productCategory=Defrosted Fish',
		'http://arabind.com/arabind/home/home.action?productCategory=Meat&productCategory=Meat_lebanese&productCategory=Chicken',
		'http://arabind.com/arabind/home/home.action?productCategory=Fresh Fish',
		'http://arabind.com/arabind/home/home.action?productCategory=Live Fish',
		'http://arabind.com/arabind/home/home.action?productCategory=Frozen Fish',
		'http://arabind.com/arabind/home/home.action?productCategory=Smoked Fish'
	]

	def parse(self, response):
		fishes = response.xpath('//div[@class="product1_bi"]')
		for fish in fishes:
			name = fish.xpath('.//div[@class="fishname"]/b/text()').extract_first()
			price = fish.xpath('.//div[@class="rate"]/script/text()').extract_first().lstrip("document.write(").rstrip(".toFixed(2));")
			currency_per_unit = fish.xpath('.//div[@class="rate"]/text()').extract_first().replace('\r\n','').strip().replace(' ','')
			yield { 'name': name, 'price': price + " " + currency_per_unit}

