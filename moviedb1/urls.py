from django.conf.urls import url
from . import views

urlpatterns = [ url(r'^listmovie/$', views.list_all),
                url(r'^addmovie/$', views.add_movie),
                url(r'^searchmovie/$', views.search_movie),
                url(r'^home/$', views.home),
                   ]
