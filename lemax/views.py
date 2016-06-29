from django.shortcuts import render
from django.template import context
from django.utils import timezone
from .models import News


def home(request):
    news = News.objects.all()
    range_news = range(News.objects.count())
    return render(request, 'lemax/home.html', {'news': news, 'range_news': range_news})
