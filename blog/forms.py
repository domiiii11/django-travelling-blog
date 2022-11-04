from concurrent.futures import InvalidStateError
from django import forms
from blog.models import PlaceToVisit, Post, Image
import datetime

# choices_ = PlaceToVisit.objects.all()
# choices__ = [(place_to_visit.id , place_to_visit.places_to_visit) for place_to_visit in choices_]
choices__ = []

class ImageForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    place_to_visit = forms.MultipleChoiceField(label='PlaceToVisit', choices=choices__)
    image = forms.ImageField()

class PlaceToVisitForm(forms.Form):
    place_to_visit = forms.CharField(label='Place to visit', max_length=100)
    country_name = forms.CharField(label='Country', max_length=100)

class PostForm(forms.Form):
    author = forms.CharField(label='Author', max_length=100)
    post_title = forms.CharField(label='Post title', max_length=100)
    post_text = forms.CharField(label='Post text', max_length=3000)
    # release_date = forms.DateField(label='Release date', initial=datetime.date.today)
    place_to_visit = forms.MultipleChoiceField(label='Place to visit', choices=choices__)

