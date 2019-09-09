# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
class TutsplusSpider(CrawlSpider):
    name = 'tutsplus'
    allowed_domains = ['tutsplus.com']
    start_urls = ['https://code.tutsplus.com/categories/']
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//a[@class='alphadex__item-link']"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//a[@class='pagination__button pagination__next-button']"), callback='parse_item', follow=True)
    )
    def parse_item(self, response):
        
        # category_name=response.xpath("//*[@class='content-banner__title-breadcrumb-category']")
        # course_name=response.xpath(//*[@class='nolinks']/text()).extract()
        # course_url=response.xpath(".//a[@class='posts__post-title ']/@href")
        # all_courses=response.xpath(".//*[@class='posts__post']")
        for tutorial in response.xpath("//li[@class='posts__post']"):
            yield{
                "category"   : response.xpath(".//*[@class='content-banner__title-breadcrumb-category/text()']").extract_first(),
                "course_name": tutorial.xpath(".//a[@class='posts__post-title '] /h1/text()").extract_first(),
                "course_url" : tutorial.xpath(".//a[@class='posts__post-title ']/@href").extract_first() 
            }