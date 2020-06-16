from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'is_published', 'price', 'list_date', 'seller')
    list_display_links = ('id', 'brand', 'seller')
    list_filter = ('seller', )
    list_editable = ('is_published',)
    search_fields = ('brand', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25
    
admin.site.register(Listing, ListingAdmin)
