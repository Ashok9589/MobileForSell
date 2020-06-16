from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from . models import Contact

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        seller_email = request.POST['seller_email']
        
        #Check if user has made Inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an  Inquiry regarding this ! A Seller will get back to you soon regarding this')
                return redirect('/listings/'+listing_id)
        
        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id )

        contact.save()
        
        #Send Email
        send_mail(
            'Inquiry for your ' + listing,
            'There has been an Inquiry for your device named ' + listing + '.\n\n Name : ' + name + ' \n Email : ' + email + '\n Phone : ' + phone + '\n Message : ' + message + '\n\nFor more information please Sign In into the Admin Panel For more Info',
            'didyouknowthisfacts@gmail.com',
            [seller_email, 'ashokmali1999@gmail.com'],
            fail_silently=False
        )
        
        messages.success(request, 'Your request has been submitted ! A Seller will get back to you soon' )
        return redirect('/listings/'+listing_id)
        