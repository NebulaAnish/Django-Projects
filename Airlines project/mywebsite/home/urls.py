from . import views
from django.urls import path

urlpatterns = [
    path("", views.index),
    path("home", views.index),
    path('contact', views.contact),
    path('portfolio', views.portfolio),
    path('services', views.services),

]
