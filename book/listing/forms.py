from django.forms import ModelForm
from.models import Listing

class ListingForm(ModelForm):
   class Meta:
      model = Listing
      fields = [
      "title",
      "author",
      "price",
      "ratings",
      ]
   