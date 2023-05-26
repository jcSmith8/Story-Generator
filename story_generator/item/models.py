from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name
    
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name ='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    main_character = models.CharField(max_length=255, null=True)
    place = models.CharField(max_length=255)
    time_period = models.CharField(max_length=255)
    length = models.TimeField(auto_now=True)
    theme = models.CharField(max_length=255)
    image = models.ImageField(upload_to='item_images', blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(User, related_name='items', on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name