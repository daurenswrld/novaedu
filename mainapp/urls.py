from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('map/', map, name='map'),
    path('team/', team, name='team'),
    path('offices/', offices, name='offices'),
    path('contacts/', contacts, name='contacts'),
    path('events/', EventsPage.as_view(), name='events'),
    path('latest/', LatestNews.as_view(), name='latest'),
    path('news/', NewsPage.as_view(), name='news'),
    path('news/<int:news_id>/', show_news, name='news_inside'),
    path('universities/uk-universities', uk, name='uk'),
    path('universities/czech-universities', czech, name='czech'),
    path('universities/poland-universities', poland, name='poland'),
    path('universities/lithuania-universities', lithuania, name='lithuania'),
    path('universities/switzerland-universities', switzerland, name='switzerland'),
    path('universities/hungary-universities', hungary, name='hungary'),
    path('universities/estonia-universities', estonia, name='estonia'),
    path('universities/georgia-universities', georgia, name='georgia'),
    path('universities/china-universities', china, name='china'),
    path('universities/south-korea-universities', south_korea, name='south_korea'),
    path('universities/hong-kong-universities', hong_kong, name='hong_kong'),
]

