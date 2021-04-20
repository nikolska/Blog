from django.urls import path

from .views import ArticlesListView


app_name = 'articles'

urlpatterns = [
	path('', ArticlesListView.as_view(), name='articles'),
]
