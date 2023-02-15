from django.urls import path
from hexlet_django_blog.article.views import IndexView, ArticleView


urlpatterns = [
    # path('', views.ArticleIndexPage.as_view())
    path('', IndexView.as_view()),
    path('<int:id>/', ArticleView.as_view(), name='show_article')
]
