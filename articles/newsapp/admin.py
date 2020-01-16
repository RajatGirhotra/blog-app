from django.contrib import admin
from django import forms
from django.forms import ModelForm

from newsapp.models import Customer, Category, Tag, Article



class ArticleForm(forms.ModelForm):
    

    class Meta:
      model = Article
      fields = (
          'headline','subtitle', 'text','category','tag', 'customer', 'image', 'slug' 
          # other fields
      )
      
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm




class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    list_display = ['headline', 'category']
    list_filter  = ('category',)
    search_fields = ( 'category__name', 'customer__name', 'tag__name')


admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin,)
