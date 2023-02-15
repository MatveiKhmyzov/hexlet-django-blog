# from hexlet_django_blog.views import IndexPage
from django.shortcuts import render
from django.http import HttpResponse
from hexlet_django_blog.article.models import Article
from django.views import View

articles = [
    {'article_id': 1, 'tag': 'ruby'},
    {'article_id': 34, 'tag': 'go'},
    {'article_id': 42, 'tag': 'python'},
    {'article_id': 47, 'tag': 'java'},
    {'article_id': 50, 'tag': 'c++'},
]


# class ArticleIndexPage(IndexPage):
#     template_name = 'article/index.html'
# 
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Articles'
#         return context


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'article/index.html', context={
            'articles': articles})


# def index(request, tag, article_id):
#     for elem in articles:
#         if elem['article_id'] == article_id and elem['tag'] == tag:
#             return render(
#                 request,
#                 'article/index.html',
#                 context=elem)

