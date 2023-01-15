from django.shortcuts import render,redirect
from .models import Listing
from .forms import ListingForm
# Create your views here.

# list view
def listing_list(request):
    listings = Listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, "listing_list.html", context)

# retrieve view
def listing_retrieve(request,pk):
    listing = Listing.objects.get(id=pk)
    context = {
       "listing":listing
    }
    return render(request,"listing_retrieve.html",context)

# Create View
def listing_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form":form
    }
    return render(request,"listing_create.html",context)

def listing_update(request,pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)
    if request.method == "POST":
        form = ListingForm(request.POST,instance=listing)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form":form
    }
    return render(request,"listing_update.html",context)

## Delete View
def listing_delete(request,pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect("/")