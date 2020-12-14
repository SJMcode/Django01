from django.urls import path,include
from . import views

urlpatterns = [
    path('namaste/', views.homePageView, name='Home'),
    path('about/', views.homePageView, name='Home_Namaste'),
]