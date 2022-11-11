from django.urls import path

from . import views
urlpatterns = [
    path('home/',views.home,name='predict_college-home')

]