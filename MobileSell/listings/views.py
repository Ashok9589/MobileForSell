from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, brand_choices, ram_choices, storage_choices, color_choices, os_choices, city_choices, state_choices , battery_choices, frontcam_choices, rearcam_choices, display_refresh_rate_choices, cable_choices
from sellerforms.models import SellerData
from .models import Listing 
from sellers.models import Seller

def index(request):
    sdata = SellerData.objects.all()

    paginator = Paginator(sdata, 9)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'sdata': paged_listings 
    }
    return render(request,'listings/slisting.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request,'listings/listing.html', context)
    
def slisting(request, listing_id):
    slisting = get_object_or_404(SellerData, pk=listing_id)
    mvp_sellers = Seller.objects.all().filter(is_mvp=True)

    context = {
        'listing': slisting,
        'mvp_sellers': mvp_sellers
    }

    return render(request,'listings/listing.html', context)
    

def search(request):
    queryset_list = SellerData.objects.order_by('-list_date')

    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    #price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    #brand
    if 'brand' in request.GET:
        brand = request.GET['brand']
        if brand:
            queryset_list = queryset_list.filter(brand__iexact=brand)
    
    #model_name
    if 'modelname' in request.GET:
        modelname = request.GET['modelname']
        if modelname:
            queryset_list = queryset_list.filter(modelname__iexact=modelname)

    #ram
    if 'ram' in request.GET:
        ram = request.GET['ram']
        if ram:
            queryset_list = queryset_list.filter(ram__iexact=ram)

    #storage
    if 'storage' in request.GET:
        storage = request.GET['storage']
        if storage:
            queryset_list = queryset_list.filter(storage__iexact=storage)

    #color
    if 'color' in request.GET:
        color = request.GET['color']
        if color:
            queryset_list = queryset_list.filter(color__iexact=color)

    '''
    #processor
    if 'processor' in request.GET:
        processor = request.GET['processor']
        if processor:
            queryset_list = queryset_list.filter(processor__iexact=processor)
    '''

    #os
    if 'os' in request.GET:
        os = request.GET['os']
        if os:
            queryset_list = queryset_list.filter(os__iexact=os)

    #battery
    if 'battery' in request.GET:
        battery = request.GET['battery']
        if battery:
            queryset_list = queryset_list.filter(battery__lte=battery)

    #frontcam
    if 'frontcam' in request.GET:
        frontcam = request.GET['frontcam']
        if frontcam:
            queryset_list = queryset_list.filter(frontcam__lte=frontcam)

    #rearcam
    if 'rearcam' in request.GET:
        rearcam = request.GET['rearcam']
        if rearcam:
            queryset_list = queryset_list.filter(rearcam__iexact=rearcam)

    #Display Refresh Rate
    if 'displayrefreshrate' in request.GET:
        displayrefreshrate = request.GET['displayrefreshrate']
        if displayrefreshrate:
            queryset_list = queryset_list.filter(displayrefreshrate__lte=displayrefreshrate)
    
    #Cable choices
    if 'cable' in request.GET:
        cable = request.GET['cable']
        if cable:
            queryset_list = queryset_list.filter(cable__iexact=cable)

    #city choices
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    #state choices
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)
    

    context = {
        'ram_choices': ram_choices , 
        'brand_choices': brand_choices ,
        'price_choices': price_choices ,
        'storage_choices': storage_choices , 
        'color_choices': color_choices ,
        #'processor_choices': processor_choices ,
        'os_choices': os_choices , 
        'battery_choices': battery_choices ,
        'frontcam_choices': frontcam_choices ,
        'rearcam_choices': rearcam_choices , 
        'display_refresh_rate_choices': display_refresh_rate_choices ,
        'cable_choices': cable_choices ,
        'city_choices': city_choices ,
        'state_choices': state_choices ,
        'listings' : queryset_list ,
        'values' : request.GET
    }
    return render(request,'listings/search.html', context)