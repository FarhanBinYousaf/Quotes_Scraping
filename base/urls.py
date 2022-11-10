from django.urls import path
from . import views
from .views import QuotesListView

urlpatterns = [
    path('',QuotesListView.as_view(),name="index"),
    path('run_spider',views.run_spider,name='run_spider'),
    path('quote/<int:pk>/',views.myQuote,name='quote'),
]