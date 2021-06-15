from django.urls import path
from . import views

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('today',views.daily_news,name = 'newsToday'),
    path('past_news/(\d{4}-\d{2}-\d{2}) $',views.past_news,name ='pastNews')
]