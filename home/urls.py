from django.urls import path
from .import views
urlpatterns=[
    path('',views.index),
    path('aboutus/',views.aboutus),
    path('contact/',views.contact),
    path('services/',views.services),
    path('songdetails/',views.songdetails),
    ]
