from django.db import models
from datetime import datetime
from sellers.models import Seller

class Listing(models.Model): 
    seller = models.ForeignKey(Seller,on_delete=models.DO_NOTHING)
    brand = models.CharField(max_length=200)
    modelname = models.CharField(max_length=100)
    price = models.IntegerField()
    ram = models.IntegerField()
    storage = models.IntegerField()
    color = models.CharField(max_length=20)
    os = models.CharField(max_length=20)
    battery = models.IntegerField()
    frontcam = models.IntegerField()
    rearcam = models.IntegerField()
    displayrefreshrate = models.IntegerField()
    cable = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='media/%d/')
    photo_1 = models.ImageField(upload_to='media/' , blank = True)
    photo_2 = models.ImageField(upload_to='media/' , blank = True)
    photo_3 = models.ImageField(upload_to='media/' , blank = True)
    photo_4 = models.ImageField(upload_to='media/' , blank = True)
    photo_5 = models.ImageField(upload_to='media/' , blank = True)
    photo_6 = models.ImageField(upload_to='media/' , blank = True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default = datetime.now , blank = True)
    def __str__(self):
        return self.brand
