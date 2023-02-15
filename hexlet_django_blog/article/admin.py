from django.contrib import admin
from .models import Article
from django.contrib.admin import DateFieldListFilter


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['name', 'body']
    list_display = ('name', 'body')
    list_filter = (('timestamp', DateFieldListFilter),)


