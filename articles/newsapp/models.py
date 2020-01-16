from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=25, default = None)
    
    def __str__(self):
        return self.name
        
    class Meta:
             verbose_name_plural = "Customers"

class Category(models.Model):
    name = models.CharField(max_length = 25)
    
    def __str__(self):
        return self.name
    
    class Meta:
             verbose_name_plural = "Categories"
    
class Tag(models.Model):
    name = models.CharField(max_length = 25)
    
    def __str__(self):
        return self.name 
    
    class Meta:
             verbose_name_plural = "Tags"   
    
class Article(models.Model):
    headline = models.CharField(max_length=60)
    slug     = models.SlugField()
    subtitle = models.TextField(max_length=100)
    text     = models.TextField(max_length=5000)
    pub_date = models.DateField(auto_now_add = True)
    image    = models.ImageField(default= None)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE,)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    tag      = models.ManyToManyField(Tag)
    
    
    def __str__(self):
        return self.headline
    
    class Meta:
             verbose_name_plural = "Articles"
    
    
    



    