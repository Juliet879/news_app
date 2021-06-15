from django.shortcuts import redirect, render
from django.http  import HttpResponse
from django.http import HttpResponse,Http404 
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')


def daily_news(request):
    date = dt.date.today()
    return render(request,'all-news/today_news.html',{"date":date,})

# def days_converter(dates):
#     # Function that gets the weekday number from the date.
#     day_number = dt.date.weekday(dates)

#     days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

#     # returning the actual da of the week
#     day = days[day_number]
#     return day

def past_news(request,past_date):
    # Convert date from string url
    try:
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(daily_news)

    return render(request,'all-news/past_news.html',{"date":date})