from django.urls import path,include

from crawler import views;
urlpatterns= [
    path('',views.index,name="index"),
]