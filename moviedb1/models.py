from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms


class Movie(models.Model):

    NONE = 'None'
    HORROR = 'horror'
    COMEDY = 'comedy'
    ACTION = 'action'
    DRAMA = 'drama'

    GENRE_CHOICES = (
        (NONE,'None'),
        (HORROR, 'Horror'),
        (COMEDY, 'Comedy'),
        (ACTION, 'Action'),
        (DRAMA, 'Drama')
    )

    title = models.CharField(max_length=32)
    language = models.CharField(max_length=10)
    country = models.CharField(max_length=16)
    genre = models.CharField(max_length=10,choices=GENRE_CHOICES)
    rating = models.IntegerField(default=0,validators=[MaxValueValidator(10), MinValueValidator(0)],help_text="""values between 0 to 10""")

    def __str__(self):
        return '%s' % self.title


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ["title", "country", "genre", "language","rating"]



