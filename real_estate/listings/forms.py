from django.forms import ModelForm, Form
from .models import Listings


class ListingForm(ModelForm):
    class Meta:
        model = Listings
        fields = [
            'title',
            'price',
            'num_of_bedrooms',
            'num_of_bathrooms',
            'area',
            'address',
            'image',
        ]
