from django.shortcuts import (render,
                              get_object_or_404,
                              redirect)
from hexlet_django_blog.article.models import Article
from django.views import View
from .forms import ArticleForm
from django.contrib import messages
from django.db.models import Q


class IndexView(View):

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')
        articles = Article.objects.filter(Q(name__icontains=query))
        return render(request, 'article/index.html', context={
            'articles': articles,
            'query': query,
        })

    # def get(self, request, *args, **kwargs):
    #     articles = Article.objects.all()[:15]
    #     return render(request, 'article/index.html', context={
    #         'articles': articles})


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'article/show.html', context={
            'article': article,
        })


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        messages = ''
        return render(request, 'article/create.html', {'form': form, 'messages': messages})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статья добавлена')
            return redirect('article_list')
        messages.error(request, 'Ошибка')
        return render(request, 'article/create.html', {'form': form})


class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'article/update.html', {'form': form, 'article_id': article_id})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Изменения применены')
            return redirect('article_list')
        messages.error(request, 'Ошибка')
        return render(request, 'article/update.html', {'form': form, 'article_id': article_id})


class ArticleFormDestroyView(View):

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST)
        if form:
            article.delete()
        return redirect('article_list')
