from django.contrib import admin

from .models import Post, PlaceToVisit, Image

admin.site.register(Post)
admin.site.register(PlaceToVisit)
admin.site.register(Image)