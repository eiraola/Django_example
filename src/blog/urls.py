from django.contrib import admin
from django.urls import path, include
from src.blog.views import article_create_view, article_lookup_view, article_list, ArticleListView, ArticleDetailView
urlpatterns = [
    path('', article_create_view, name='blogC'),
    path('article/<int:my_id>', article_lookup_view, name='article-detail'),
    path('article/list', article_list, name='articlelist'),
    path('article/2list', ArticleListView.as_view(), name='articlelist2'),
    path('article/2det/<int:pk>', ArticleDetailView.as_view(), name='detaillist')

]
