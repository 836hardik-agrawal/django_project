from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'predict_college/home.html')
# Create your views here.
