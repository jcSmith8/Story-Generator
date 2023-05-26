from django.shortcuts import render

from item.models import Category, Item

# Create your views here.
def index(request):
    items = Item.objects.filter()[0:3]
    categories = Category.objects.all()
    return render(request, 'core/index.html',{
        'category': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')