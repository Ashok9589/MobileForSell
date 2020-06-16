from django.db import models

from datetime import datetime

class SellerData(models.Model):
    sname = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=30,null=True)
    brand = models.CharField(max_length=200,null=True)
    modelname = models.CharField(max_length=100, null=True)
    price = models.IntegerField(null=True)
    ram = models.IntegerField(null=True)
    storage = models.IntegerField(null=True)
    color = models.CharField(max_length=20,null=True)
    os = models.CharField(max_length=20,null=True)
    battery = models.IntegerField(null=True)
    frontcam = models.IntegerField(null=True)
    rearcam = models.IntegerField(null=True)
    displayrefreshrate = models.IntegerField(null=True)
    cable = models.CharField(max_length=30,null=True)
    city = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/' , blank = True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/' , blank = True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/' , blank = True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/' , blank = True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/' , blank = True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/' , blank = True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default = datetime.now , blank = True)
    
    def __str__(self):
        return self.sname