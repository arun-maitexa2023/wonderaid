from django.db import models

# Create yourmodelss here.

class log(models.Model):
    username = models.CharField(max_length = 50,unique = True)
    password =models.CharField(max_length = 50,unique = True)
    role =models.CharField(max_length = 50)
    def __str__(self):
        return self.username

class user(models.Model):
    fullname =models.CharField(max_length = 50,null= True)
    name =models.CharField(max_length = 50)
    userdob =models.CharField(max_length = 50,null = True)
    usergender =models.CharField(max_length = 50,null = True)
    userphone = models.CharField(max_length  = 50)
    usermail =models.CharField(max_length = 50)
    userplace =models.CharField(max_length = 50,null = True)
    userpincode =models.CharField(max_length = 50,null = True)
    userpassword =models.CharField(max_length = 50)
    userdp =  models.ImageField(upload_to='images/',null=True)
    role =models.CharField(max_length = 50)
    userstatus=models.CharField( max_length =  50)
    login=models.ForeignKey(log, on_delete=models.CASCADE)
    
   

    def __str__(self):
        return self.name

class Hotel(models.Model):
    hotelname=models.CharField(max_length = 50)
    hotelphone =models.CharField(max_length = 50)
    hotelmail=models.CharField(max_length = 50)
    hotellocation=models.CharField(max_length = 50,null=True)
    hotelpincode =models.CharField(max_length = 50,null=True)
    hotelrating =models.CharField(max_length = 50,null=True)
    hotelrooms=models.CharField(max_length = 50,null=True)
    hotelcategory=models.CharField(max_length = 50,null=True)
    hotelfecilities = models.CharField(max_length = 50,null=True)
    hotelpackages = models.CharField(max_length = 50,null=True)
    hotelservices = models.CharField(max_length = 50,null=True)
    hoteltiming = models.CharField(max_length = 50,null=True)
    specialoffers = models.CharField(max_length = 50,null=True)
    roomsavailability = models.CharField(max_length = 50,null=True)
    description = models.CharField(max_length = 50,null=True)
    nba = models.CharField(max_length = 50,null=True)
    policies = models.CharField(max_length = 50,null=True)
    hotelpass = models.CharField(max_length = 50)
    menu = models.CharField(max_length = 50,null=True)
    reviews = models.CharField(max_length = 50,null=True)
    images = models.ImageField(upload_to='images/',null=True)
    role =models.CharField(max_length = 50)
    hotelstatus=models.CharField( max_length =  50)
    login=models.ForeignKey(log, on_delete=models.CASCADE)

    def __str__(self):
        return self.hotelname

class Restaurent(models.Model):
    restaurentname=models.CharField(max_length = 50)
    restaurentphone =models.CharField(max_length = 50)
    restaurentmail=models.CharField(max_length = 50)
    restaurentlocation=models.CharField(max_length = 50,null=True)
    restaurentpin =models.CharField(max_length = 50,null=True)
    restaurentrating =models.CharField(max_length = 50,null=True)
    restaurentcategory=models.CharField(max_length = 50,null=True)
    restaurentmenu = models.CharField(max_length = 50,null=True)
    specialoffers = models.CharField(max_length = 50,null=True)
    specials = models.CharField(max_length = 50 ,null=True)
    description = models.CharField(max_length = 50,null=True)
    nba = models.CharField(max_length = 50 ,null=True)
    policies = models.CharField(max_length = 50,null=True)
    diningoptions =models.CharField(max_length = 50,null=True)
    restaurenttiming = models.CharField(max_length = 50,null=True)
    restaurentpass = models.CharField(max_length = 50)
    reviews = models.CharField(max_length = 50,null=True)
    images = models.ImageField(upload_to='images/',null=True)
    role =models.CharField(max_length = 50)
    Restaurentstatus=models.CharField( max_length =  50)
    login=models.ForeignKey(log, on_delete=models.CASCADE)

    

    def __str__(self):
        return self.restaurentname


class Resort(models.Model):
    resortname=models.CharField(max_length = 50)
    resortphone =models.CharField(max_length = 50)
    resortmail= models.CharField(max_length =50)
    resortlocation=models.CharField(max_length = 50,null=True)
    resortpincode =models.CharField(max_length = 50,null=True)
    resortrating =models.CharField(max_length = 50,null=True)
    resortrooms=models.CharField(max_length = 50,null=True)
    resortcategory=models.CharField(max_length = 50,null=True)
    resortpackages = models.CharField(max_length = 50,null=True)
    resortservices = models.CharField(max_length = 50,null=True)
    resortfecilities= models.CharField(max_length = 50,null=True)
    resorttiming = models.CharField(max_length = 50,null=True)
    specialoffers = models.CharField(max_length = 50,null=True)
    availability = models.CharField(max_length = 50,null=True)
    description = models.CharField(max_length = 50,null=True)
    nba = models.CharField(max_length = 50,null=True)
    policies = models.CharField(max_length = 50,null=True)
    accomodationtypes = models.CharField(max_length = 50,null=True)
    accomodationdesc = models.CharField(max_length = 50,null=True)
    foodmenu= models.CharField(max_length = 50,null=True)
    diningoptions = models.CharField(max_length = 50,null=True)
    pricing = models.CharField(max_length = 50,null=True)
    reviews = models.CharField(max_length = 50,null=True)
    images = models.ImageField(upload_to='images/',null=True)
    resortpass = models.CharField(max_length = 50)
    role = models.CharField(max_length = 50)
    resortstatus = models.CharField( max_length =  50)
    login=models.ForeignKey(log, on_delete=models.CASCADE)

    def __str__(self):
        return self.resortname
    
class Travels(models.Model):
    travelsname=models.CharField(max_length = 50)
    travelsphone =models.CharField(max_length = 50)
    travelsmail =models.CharField(max_length = 50)
    travelslocation=models.CharField(max_length = 50,null=True)
    travelspincode =models.CharField(max_length = 50,null=True)
    travelsrating =models.CharField(max_length = 50,null=True)
    travelspackages =models.CharField(max_length = 50,null=True)
    travelstiming = models.CharField(max_length = 50,null=True)
    travelspass = models.CharField(max_length = 50,null=True)
    policies = models.CharField(max_length = 50,null=True)
    reviews = models.CharField(max_length = 50,null=True)
    images = models.ImageField(upload_to='images/',null=True)
    role =models.CharField(max_length = 50)
    travelsstatus=models.CharField( max_length =  50)
    login=models.ForeignKey(log, on_delete=models.CASCADE)


    def __str__(self):
        return self.travelsname

class Guide(models.Model):
    guidename=models.CharField(max_length = 50)
    guidephone =models.CharField(max_length = 50)
    guidemail = models.CharField(max_length = 50)
    guidelocation=models.CharField(max_length = 50,null=True)
    guidepincode =models.CharField(max_length = 50,null=True)
    guiderating =models.CharField(max_length = 50,null=True)
    Reviews = models.CharField(max_length = 50,null=True)
    guiderepass = models.CharField(max_length = 50)
    guidedp =  models.ImageField(upload_to='images/',null=True)
    role =models.CharField(max_length = 50)
    Guidesstatus=models.CharField( max_length =  50)
    login=models.ForeignKey(log, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.guidename