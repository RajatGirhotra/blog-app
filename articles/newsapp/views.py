from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Article
from newsapp.models import Article



class ArticleListView(ListView):
    template_name = 'newsapp/index.html'
    model = Article
    
    context_artcile_name = 'Article'
    queryset = Article.objects.all().order_by('pub_date')
    
    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['now'] = Article.objects.all().order_by('pub_date')
        return context


class ArticleDetailView(DetailView):
    model = Article
    
    template_name = 'newsapp/detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = Article.objects.all()
        return context
