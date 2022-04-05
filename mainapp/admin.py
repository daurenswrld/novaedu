from django.contrib import admin
from .models import *

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','time_create','is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published',)

admin.site.register(News, NewsAdmin)
admin.site.register(Events, NewsAdmin)
# Register your models here.
