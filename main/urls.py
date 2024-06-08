from django.urls import path
from django.contrib.auth import views as auth_views

from . import views as home_views

app_name = 'main'

urlpatterns = [
    path('', home_views.home_page, name='home_page'),
]