import datetime
from django.db import models
from django.utils import timezone


class PlaceToVisit(models.Model):    
    places_to_visit = models.CharField(max_length=300)
    country_name = models.CharField(max_length=300)
        
    def __str__(self):
        return self.places_to_visit  

class Post(models.Model):
    author = models.CharField(max_length=300)
    post_title = models.CharField(max_length=300)
    post_text = models.CharField(max_length=5000)
    release_date = models.DateTimeField(auto_now=True)
    places_to_visit = models.ForeignKey(PlaceToVisit, on_delete=models.CASCADE)
    

    def __str__(self):
        date = str(self.release_date)
        return date

    def was_published_recently(self):
        return self.release_date >= timezone.now() - datetime.timedelta(days=1)


class Image(models.Model): 
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to="media/")
    places_to_visit = models.ForeignKey(PlaceToVisit, on_delete=models.CASCADE)


    def __str__(self):
        return self.title   