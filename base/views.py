from django.shortcuts import render,HttpResponse, redirect
import scrapydo
import os
from secondPractice.spiders.quotes_spider import QuotesSpider
from twisted.internet import reactor
from scrapy.crawler import Crawler,CrawlerRunner
from scrapy.settings import Settings
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from .models import Quotes
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView

 # the script will block here until the crawling is finished
# Create your views here.

def Index(request):
    quote_list = Quotes.objects.all()
    context={'quote_list':quote_list}
    return render(request,'base/main.html',context)
    
def myQuote(request,pk):
    single_quote = Quotes.objects.get(pk=pk)
    context = {'single_quote':single_quote}
    return render(request,'base/singleQuote.html',context)
    
class QuotesListView(ListView):
    model = Quotes
    template_name = 'base/main.html'
    context_object_name = 'quote_list'
    paginate_by = 10


def run_spider(quotes):

    crawler_settings = Settings()
    scrapydo.setup()
    scrapydo.run_spider(QuotesSpider, asin_number=quotes)
    return HttpResponse('Scraping............')
