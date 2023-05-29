from django.shortcuts import render

from item.models import Category, Item

# Create your views here.
# def index(request):
#     items = Item.objects.filter()[0:3]
#     categories = Category.objects.all()
#     return render(request, 'core/index.html',{
#         'category': categories,
#         'items': items,
#     })

from django.shortcuts import render
from .models import StoryInfoDjango, StoryForm


def index(request):
    submitbutton= request.POST.get("submit")

    characters = ''
    mainchar = ''
    place = ''
    time = ''
    wordCount = ''
    theme = ''
    audience = ''


    form = StoryForm(request.POST or None)
    if form.is_valid():
        
        characters = form.cleaned_data.get(characters)
        mainchar = form.cleaned_data.get(mainchar)
        place = form.cleaned_data.get(place)
        time = form.cleaned_data.get(time)
        wordCount = form.cleaned_data.get(wordCount)
        theme = form.cleaned_data.get(theme)
        audience = form.cleaned_data.get(audience)

    form.save()

    context= {'form': form, 'characters': characters, 'mainchar':mainchar, 'place':place,
              'time':time, 'wordCount':wordCount, 'theme':theme, 'audience':audience}
        
    return render(request, 'core/index.html', context)
