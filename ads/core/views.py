from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")
def page(request):
    return render(request, "ggg.html")
def catalog(request):
    return render(request, "catalog.html")
    