from django.shortcuts import (render,
                              get_object_or_404,
                              redirect)
from hexlet_django_blog.article.models import Article
from django.views import View
from .forms import ArticleForm
from django.contrib import messages


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'article/index.html', context={
            'articles': articles})


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
            messages.success(request, 'Success')
            return redirect('article_list')
        messages.error(request, 'Error')
        return render(request, 'article/create.html', {'form': form})
