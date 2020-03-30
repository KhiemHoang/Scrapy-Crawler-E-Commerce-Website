# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class CrawlerPipeline(object):
    def __init__(self):
        self.myCsv = csv.writer(open('Hot_Deal.txt', 'w', encoding='utf-8'))
        self.myCsv.writerow({"==============**** TGDĐ HOT DEAL ****==============="})

    def process_item(self, item, spider):
        self.myCsv.writerow({"-----------------"})
        self.myCsv.writerow(["Name: " + item['Title']])

        #Print Deal_Price
        if item['Deal'] == None:
            self.myCsv.writerow({"Deal Price: Not update"})
        else:
            self.myCsv.writerow(["Deal Price: " + item['Deal']])

        #Print Real_Price
        if item['Real_Price'] == None:
            self.myCsv.writerow({"Origin Price: Not update"})
        else:
            self.myCsv.writerow(["Origin Price: " + item['Real_Price']])

        #Print Rate
        if item['Rate'] == None:
            self.myCsv.writerow({"Rate: No comment"})
        else:
            self.myCsv.writerow(["Number of Comments: " + item['Rate']])

        self.myCsv.writerow({" "})
        return item

    #def process_item(self, item, spider):
        #return item
