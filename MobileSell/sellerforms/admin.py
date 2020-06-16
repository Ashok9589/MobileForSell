from django.contrib import admin
from .models import SellerData

class SellerDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'sname', 'brand', 'price', 'list_date')
    list_display_links = ('id', 'brand', 'sname')
    list_filter = ('sname', 'brand', )
    list_per_page = 25


admin.site.register(SellerData, SellerDataAdmin)
