from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, brand_choices, city_choices, state_choices, ram_choices, storage_choices, color_choices, os_choices, battery_choices, frontcam_choices, rearcam_choices, display_refresh_rate_choices, cable_choices


from listings.models import Listing
from sellers.models import Seller
from sellerforms.models import SellerData

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    sellerdata = SellerData.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': sellerdata ,
        'ram_choices': ram_choices , 
        'brand_choices': brand_choices ,
        'price_choices': price_choices ,
        'storage_choices': storage_choices , 
        'color_choices': color_choices ,
        'os_choices': os_choices , 
        'battery_choices': battery_choices ,
        'frontcam_choices': frontcam_choices ,
        'rearcam_choices': rearcam_choices , 
        'display_refresh_rate_choices': display_refresh_rate_choices ,
        'cable_choices': cable_choices ,
        'city_choices': city_choices ,
        'state_choices': state_choices ,
    }

    return render(request,'pages/index.html', context)

def about(request):
    #get all sellers
    sellers = Seller.objects.order_by('-join_date')

    #Get MVP
    mvp_sellers = Seller.objects.all().filter(is_mvp=True)

    context = {
        'sellers': sellers ,
        'mvp_sellers': mvp_sellers
    }

    return render(request,'pages/about.html', context)  

