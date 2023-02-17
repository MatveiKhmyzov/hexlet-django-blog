from django.urls import path
from hexlet_django_blog.article.views import (
                                        IndexView,
                                        ArticleView,
                                        ArticleFormCreateView
)


urlpatterns = [
    # path('', views.ArticleIndexPage.as_view())
    path('', IndexView.as_view(), name='article_list'),
    path('<int:id>/', ArticleView.as_view(), name='show_article'),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
    # path('<int:id>/comment/', CommentArticleView.as_view(), name='comment_create'),
]
