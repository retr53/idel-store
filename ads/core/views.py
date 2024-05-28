from django.shortcuts import render
from .models import Moto

# Create your views here.
def home(request):
    return render(request, "home.html")
def page(request):
    return render(request, "ggg.html")
def catalog(request):
    motopoduct = Moto.objects.all()
    return render(request, "catalog.html",{'moto':motopoduct})
    