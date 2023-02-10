from django.shortcuts import render
from hexlet_django_blog.views import IndexPage


class ArticleIndexPage(IndexPage):
    template_name = 'article/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Articles'
        return context


# def index(request):
#     return render(
#         request,
#         'article/index.html',
#         context={'title': 'Articles'})

