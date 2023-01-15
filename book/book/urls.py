
from django.contrib import admin
from django.urls import path
from listing.views import (
    listing_list,
    listing_retrieve,
    listing_create,
    listing_update,
    listing_delete
    )

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", listing_list),
    path("listing/<pk>/",listing_retrieve),
    path("add_listing/",listing_create),
    path("listing/<pk>/edit/",listing_update),
    path("listing/<pk>/delete/",listing_delete),
]
