# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
    

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from base.models import Quotes
class SecondpracticePipeline(object):

    def process_item(self, item, spider):
        item.save()
        return item

# class DuplicatesPipeline:
#     itemlist = []

#     # def __init__(self): 
#     #     self.ids_seen = set() 
#     def process_item(self, item, spider):

#         if item in self.itemlist:
#             raise DropItem
#         else:
#             self.itemlist.append(item)
#         return item


        
# class DuplicatesPipeline(object):

#     def __init__(self):
#         self.title_seen = set()

#     def process_item(self, item, spider):
#         if item['title'] in self.title_seen:
#             raise DropItem("Duplicate item title found: %s" % item)
#         else:
#             # self.title_seen.add(item['id'])
#             return item
        

    

    
