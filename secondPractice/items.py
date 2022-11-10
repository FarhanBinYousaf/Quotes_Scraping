
from scrapy_djangoitem import DjangoItem
from base.models import Quotes
import scrapy


class SecondpracticeItem(DjangoItem):
    # define the fields for your item here like:

    django_model = Quotes

    # title = scrapy.Field()
    # author = scrapy.Field()
    # tag = scrapy.Field()

