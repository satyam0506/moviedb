from django.contrib import admin
from .models import Movie

# Register your models here.


class MovieAdmin(admin.ModelAdmin):

    list_display = ['title','country','rating','genre']
    search_fields = ["title"]

admin.site.register(Movie, MovieAdmin)