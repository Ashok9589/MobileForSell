from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from sellerforms.models import SellerData
from sellers.models import Seller

def sell(request):
    if request.method == 'POST':
        sname = request.POST.get("sname")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        brand = request.POST.get("brand")
        modelname = request.POST.get("modelname")
        price = request.POST.get("price")
        ram = request.POST.get("ram")
        storage = request.POST.get("storage")
        color = request.POST.get("color")
        os = request.POST.get("os")
        battery = request.POST.get("battery")
        frontcam = request.POST.get("frontcam")
        rearcam = request.POST.get("rearcam")
        displayrefreshrate = request.POST.get("displayrefreshrate")
        cable = request.POST.get("cable")
        city = request.POST.get("city")
        state = request.POST.get("state")
        description = request.POST.get("description")
        photo_main = request.FILES.get("photo_main")
        photo_1 = request.FILES.get("photo_1")
        photo_2 = request.FILES.get("photo_2")
        photo_3 = request.FILES.get("photo_3")
        photo_4 = request.FILES.get("photo_4")
        photo_5 = request.FILES.get("photo_5")
        photo_6 = request.FILES.get("photo_6")

        seller_info = SellerData(sname=sname , phone=phone, modelname=modelname , price=price, frontcam=frontcam, rearcam=rearcam, description=description, photo_main=photo_main, photo_1=photo_1, photo_2=photo_2, photo_3=photo_3, photo_4=photo_4, photo_5=photo_5, photo_6=photo_6,  battery=battery, email=email, os=os , brand=brand, ram=ram, storage=storage, color=color, displayrefreshrate=displayrefreshrate, cable=cable, city=city, state=state)
        seller_info.save()

    return render(request,'pages/sell.html') 
  
def index(request):
    slisting = SellerData.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(slisting, 3)
    page = request.GET.get('slisting')
    paged_listings = paginator.get_page(page)

    context = {
        'slisting': paged_listings 
    }
    return render(request,'listings/slisting.html', context)

def slisting(request, slisting_id):
    slisting = get_object_or_404(SellerData, pk=slisting_id)
    mvp_sellers = Seller.objects.all().filter(is_mvp=True)
    
    context = {
        'listing': slisting,
        'mvp_sellers': mvp_sellers
    }

    return render(request,'listings/listing.html', context)
