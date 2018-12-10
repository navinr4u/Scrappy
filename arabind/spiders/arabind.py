import scrapy

class AraBind(scrapy.Spider):
	name = 'arabind'
	start_urls = ['https://www.arabind.com/app/w/e/PRDTG%20C_A8126_P_A8126_T_FRESH%20FISH.htm',
		'https://www.arabind.com/app/w/e/MOREPRDTG%20P_A8126.htm?T=A8126&L=24&O=24&srt_b=',
		'https://www.arabind.com/app/w/e/MOREPRDTG%20P_A8126.htm?srt_b=&T=A8126&L=24&O=48',
		'https://www.arabind.com/app/w/e/MOREPRDTG%20P_A8126.htm?srt_b=&T=A8126&L=24&O=72',
		'https://www.arabind.com/app/w/e/MOREPRDTG%20P_A8126.htm?srt_b=&T=A8126&L=24&O=96',

	]

	def parse(self, response):
		fishes = response.xpath('//div[@class="prod-container"]')
		for fish in fishes:
			name = fish.xpath('.//div[@class="prod-label"]/a/text()').extract_first()
			price = fish.xpath('.//div[@class="price-label"]/script/text()').extract_first().lstrip("document.write(").rstrip(".toFixed(2));")
		   # currency_per_unit = fish.xpath('.//div[@class="rate"]/text()').extract_first().replace('\r\n','').strip().replace(' ','')
		   # yield { 'name': name, 'price': price + " " + currency_per_unit}
			yield { 'name': name, 'price': price }



#<div class="rate"><script>document.write(69.9.toFixed(2));</script> AED 
                                                    
                                                    #    /Kg
                                                        
                                                        
#<div class="rate"><script>document.write(31.9.toFixed(2));</script> AED 
                                                    
                                                     #   /Kg
                                                        
#<div class="rate"><script>document.write(17.9.toFixed(2));</script> AED 
                                                    
                                                      #  /Kg                                                        