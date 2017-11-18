from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import  include
from django.contrib.auth import views as auth_views
from people import views as core_views
app_name = 'people'

urlpatterns = [
    url(r'^(?P<person>[a-zA-Z0-9_]+)$', core_views.home_people, name='home_people'),
    url(r'^(?P<person>[a-zA-Z0-9_]+)/publications$', core_views.home_publications, name='home_publica')
]