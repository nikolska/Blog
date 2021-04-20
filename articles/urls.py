from django.urls import path

from .views import ArticleCreateView, ArticlesListView


app_name = 'articles'

urlpatterns = [
	path('', ArticlesListView.as_view(), name='articles'),
	path('create/', ArticleCreateView.as_view(), name='create_article'),
]
