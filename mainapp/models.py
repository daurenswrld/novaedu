from django.db import models
from django.urls import reverse

class News(models.Model):
    title = models.CharField(max_length=255 , verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Содержание')
    photo = models.ImageField(upload_to='photos/%Y', verbose_name='Фото')
    time_read = models.CharField(max_length=100, verbose_name='Время чтения')
    time_add = models.CharField(max_length=100, verbose_name='Время добавления')
    is_published = models.BooleanField(default=True,verbose_name='Опубликовано')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_inside', kwargs={'news_id': self.pk})

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"
        ordering = ['-time_create', 'title']


class Events(models.Model):
    title = models.CharField(max_length=255 ,verbose_name='Заголовок')
    content = models.TextField(blank=True,verbose_name='Содержание')
    time_add = models.CharField(max_length=100, verbose_name='Время добавления')
    is_published = models.BooleanField(default=True,verbose_name='Опубликовано')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "События"
        verbose_name_plural = "События"
        ordering = ['-time_create', 'title']
