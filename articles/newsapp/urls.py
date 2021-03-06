from django.urls import path
from . import views
from newsapp.views import ArticleListView, ArticleDetailView

app_name = 'articles'

urlpatterns = [
    path('', ArticleListView.as_view(), name = "list"),
    path('<slug:slug>/', ArticleDetailView.as_view(), name = "detail")
]
