from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'home/index.html')


def home(request):
    return render(request, 'home/index.html')


def contact(request):
    return render(request, 'home/contact/index.html')


def portfolio(request):
    return render(request, "home/portfolio/index.html")


def services(request):
    return render(request, 'home/services/index.html')
