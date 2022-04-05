from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import *
from django.core.paginator import Paginator

def index(request):
    return render(request, 'mainapp/index.html', {'title':'Главная'})

def dashboard(request):
    return render(request, 'mainapp/dashboard.html', {'title':'Статистика'})

def map(request):
    return render(request, 'mainapp/map.html', {'title':'Страны'})

def team(request):
    return render(request, 'mainapp/team.html', {'title':'Команда'})

def offices(request):
    return render(request, 'mainapp/offices.html', {'title':'Офисы'})

def contacts(request):
    return render(request, 'mainapp/contacts.html', {'title':'Контакты'})

class EventsPage(ListView):
    paginate_by = 6
    model = Events
    template_name = 'mainapp/events.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Events.objects.filter(is_published = True)

class NewsPage(ListView):
    paginate_by = 10
    model = News
    template_name = 'mainapp/news.html'
    context_object_name = 'news'
    def get_queryset(self):
        return News.objects.filter(is_published = True)


class LatestNews(ListView):
    paginate_by = 5
    model = News
    template_name = 'mainapp/latest.html'
    context_object_name = 'latest'
    def get_queryset(self):
        return News.objects.filter(is_published = True)


def show_news(request, news_id):
    news = News.objects.filter(pk=news_id)
    context = {
        'news': news,
        'title': f'Новость {news_id}',
    }
    return render(request, 'mainapp/news-inside.html', context=context)

def uk(request):
    return render(request, 'mainapp/universities/uk-universities.html', {'title':'UK'})
def czech(request):
    return render(request, 'mainapp/universities/czech-universities.html', {'title':'Czech'})
def poland(request):
    return render(request, 'mainapp/universities/poland-universities.html', {'title':'Poland'})
def lithuania(request):
    return render(request, 'mainapp/universities/lithuania-universities.html', {'title':'Lithuania'})
def switzerland(request):
    return render(request, 'mainapp/universities/switzerland-universities.html', {'title':'Switzerland'})
def hungary(request):
    return render(request, 'mainapp/universities/hungary-universities.html', {'title':'Hungary'})
def estonia(request):
    return render(request, 'mainapp/universities/estonia-universities.html', {'title':'Estonia'})
def georgia(request):
    return render(request, 'mainapp/universities/georgia-universities.html', {'title':'Georgia'})
def china(request):
    return render(request, 'mainapp/universities/china-universities.html', {'title':'China'})
def south_korea(request):
    return render(request, 'mainapp/universities/south-korea-universities.html', {'title':'South Korea'})
def hong_kong(request):
    return render(request, 'mainapp/universities/hong-kong-universities.html', {'title':'Hong Kong'})