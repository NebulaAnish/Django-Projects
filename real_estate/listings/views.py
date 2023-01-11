from django.shortcuts import render, redirect
from .models import Listings
from .forms import ListingForm
# Create your views here.
# CRUD L : Create, Retrieve, Update, Delete, List


# List
def listing_list(request):
    listings = Listings.objects.all()
    context = {
        'listings': listings
    }
    return render(request, "listings.html", context)

# Retrieve


def listing_retrieve(request, pk):
    listing = Listings.objects.get(id=pk)
    context = {
        "listing": listing
    }
    return render(request, "listing_retrieve.html", context)

# Create


def listing_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form": form
    }
    return render(request, "listing_create.html", context)

# Update


def listing_update(request, pk):
    listing = Listings.objects.get(id=pk)
    form = ListingForm(instance=listing)
    if request.method == "POST":
        form = ListingForm(request.POST, files=request.FILES, instance=listing)
        print(request.POST)
        if form.is_valid():
            form.save()

            return redirect(f"/listing/{pk}")
    context = {
        "form": form
    }
    return render(request, "listing_update.html", context)

# DELETE


def listing_delete(request, pk):
    listing = Listings.objects.get(id=pk)
    listing.delete()
    return redirect("/")
