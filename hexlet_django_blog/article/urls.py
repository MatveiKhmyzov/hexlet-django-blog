from django.urls import path
from hexlet_django_blog.article.views import (
                                        IndexView,
                                        ArticleView,
                                        ArticleFormCreateView,
                                        ArticleFormEditView,
                                        ArticleFormDestroyView
)


urlpatterns = [
    path('', IndexView.as_view(), name='article_list'),
    path('<int:id>/', ArticleView.as_view(), name='show_article'),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
    path('<int:id>/edit/', ArticleFormEditView.as_view(), name='articles_update'),
    path('<int:id>/delete/', ArticleFormDestroyView.as_view(), name='articles_destroy')
]
