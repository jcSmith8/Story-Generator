from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from django.forms import ModelForm


#myModel = MyModel()
# listIWantToStore = [1,2,3,4,5,'hello']
# myModel.myList = json.dumps(listIWantToStore)
# myModel.save()


# Create your models here.
class StoryInfoDjango(models.Model):
    characters = models.TextField()
    mainchar = models.CharField(max_length=30)
    place = models.CharField(max_length=30)
    time = models.IntegerField()
    wordCount = models.IntegerField()
    theme = models.CharField(max_length=255)
    audience = models.CharField(max_length=255)
    chapters = models.TextField(null=True) #stores chapters as JSON file, need to JSONify later
    chapterCount = models.IntegerField()
    wholeStory = models.TextField()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
        
class StoryForm(ModelForm):
    class Meta:
        model = StoryInfoDjango
        fields = ["place", "time", "characters", "mainchar", "wordCount", "theme", "audience"]
        
class RandomStoryForm(ModelForm):
    class Meta:
        model = StoryInfoDjango
        fields = ["audience", "wordCount"]