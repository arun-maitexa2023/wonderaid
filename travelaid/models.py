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
    
class Spots(models.Model):
    Spotsname=models.CharField(max_length = 50)
    Spotsclimat =models.CharField(max_length = 50)
    Bestperiod = models.CharField(max_length = 50)
    description=models.CharField(max_length = 50,null=True)
    Visiterscount =models.CharField(max_length = 50,null=True)
    Rating =models.CharField(max_length = 50,null=True)
    Area = models.CharField(max_length = 50,null=True)
    View = models.CharField(max_length = 50,null=True)
    country =  models.CharField(max_length = 50,null=True)
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    username=models.CharField(max_length = 50)
    Spots_status=models.CharField(max_length = 50)
  
    def __str__(self):
        return self.Spotsname
    
class Userprofile(models.Model):
    Patrons=models.CharField(max_length = 50)
    Average =models.CharField(max_length = 50)
    Solo = models.CharField(max_length = 50)
    Leadingcommunity=models.CharField(max_length = 50,null=True)
    Includingcommunity =models.CharField(max_length = 50,null=True)
    Nextdestination =models.CharField(max_length = 50,null=True)
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    username=models.CharField(max_length = 50)
    Userprofile_status=models.CharField(max_length = 50)
   
    def __str__(self):
        return self.username

class Plannedtrip(models.Model):
    Startingpoint=models.CharField(max_length = 50)
    Destination =models.CharField(max_length = 50)
    Days = models.CharField(max_length = 50)
    Nights=models.CharField(max_length = 50)
    Plan =models.CharField(max_length = 50,null=True)
    Guide =models.CharField(max_length = 50,null=True)
    Travels =models.CharField(max_length = 50,null=True)
    Persons =models.CharField(max_length = 50,null=True)
    Budget =models.CharField(max_length = 50,null=True)
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    username=models.CharField(max_length = 50)
    Plannedtrip_status=models.CharField(max_length = 50)

    
    def __str__(self):
        return self.Startingpoint

      #return self.Startingpoint

class Comments(models.Model):
    Commenttext=models.CharField(max_length = 50)
    Createddate =models.CharField(max_length = 50)
    spot=models.ForeignKey(Spots, on_delete=models.CASCADE)
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    username=models.CharField(max_length = 50)
    spotname=models.CharField(max_length = 50)
    Commentsstatus=models.CharField(max_length = 50)
    
    def __str__(self):
        return self.Commenttext

class Notification(models.Model):
    Sender=models.CharField(max_length = 50)
    Receiver =models.CharField(max_length = 50)
    Notification = models.CharField(max_length = 50)
    Date=models.CharField(max_length = 50)
    Action =models.CharField(max_length = 50,null=True)
    username=models.CharField(max_length = 50)
    Notificationstatus=models.CharField(max_length = 50)
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    def __str__(self):
        return self.Sender

class PackegeHotel(models.Model):

    Packegename=models.CharField(max_length = 50)
    Destination =models.CharField(max_length = 50)
    Price = models.CharField(max_length = 50)
    Startdate = models.CharField(max_length = 50)
    Enddate = models.CharField(max_length = 50)
    Bookingcount = models.CharField(max_length = 50)
    Packegestatus=models.CharField(max_length = 50)
    hotel=models.ForeignKey(Hotel, on_delete=models.CASCADE)
    hotelname=models.CharField(max_length = 50)
                    
    def __str__(self):
        return self.Packegename


class PackegeResort(models.Model):

    Packegename=models.CharField(max_length = 50)
    Destination =models.CharField(max_length = 50)
    Price = models.CharField(max_length = 50)
    Startdate = models.CharField(max_length = 50)
    Enddate = models.CharField(max_length = 50)
    Bookingcount = models.CharField(max_length = 50)
    Packegestatus=models.CharField(max_length = 50)
    Resort=models.ForeignKey(Resort, on_delete=models.CASCADE)
    resortname=models.CharField(max_length = 50)
                    
    def __str__(self):
        return self.Packegename

class PackegeTravels(models.Model):

    Packegename=models.CharField(max_length = 50)
    Destination =models.CharField(max_length = 50)
    Price = models.CharField(max_length = 50)
    Startdate = models.CharField(max_length = 50)
    Enddate = models.CharField(max_length = 50)
    Bookingcount = models.CharField(max_length = 50)
    Packegestatus=models.CharField(max_length = 50)
    Travels=models.ForeignKey(Travels, on_delete=models.CASCADE)
    travelsname=models.CharField(max_length = 50)
                    
    def __str__(self):
        return self.Packegename

class Chatcommunity(models.Model):
    Communityname=models.CharField(max_length = 50)
    Chat =models.CharField(max_length = 50)
    Createdtime = models.CharField(max_length = 50)
    Uploaddate = models.CharField(max_length = 50)
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    username=models.CharField(max_length = 50)
    Chatcommunitystatus=models.CharField(max_length = 50)    

    
    def __str__(self):
        return self.Communityname


class Reels(models.Model):
    Reelslength=models.CharField(max_length = 50)
    Reels = models.FileField(upload_to='images/',null=True)
    Description = models.CharField(max_length = 50)
    Spotname = models.CharField(max_length = 50)
    Uploaddate=models.CharField(max_length = 50)
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    username=models.CharField(max_length = 50)
        

    
    def __str__(self):
        return self.Reelslength



class Resortbooking(models.Model):
    resort=models.ForeignKey(Resort, on_delete=models.CASCADE)
    resortname=models.CharField(max_length = 50)
    noofpersons =models.CharField(max_length = 50)
    phone =models.CharField(max_length = 50)
    checkindate =models.CharField(max_length = 50)
    checkintime =models.CharField(max_length = 50)
    checkoutdate = models.CharField(max_length = 50)
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    username=models.CharField(max_length = 50)
    bookingstatus = models.CharField(max_length = 50)
                  
    def __str__(self):
        return self.resortname

class Hotelbooking(models.Model):
    hotel=models.ForeignKey(Hotel, on_delete=models.CASCADE)
    hotelname=models.CharField(max_length = 50)
    noofpersons =models.CharField(max_length = 50)
    phone =models.CharField(max_length = 50)
    checkindate =models.CharField(max_length = 50)
    checkintime =models.CharField(max_length = 50)
    checkoutdate = models.CharField(max_length = 50)
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    username=models.CharField(max_length = 50)
    bookingstatus = models.CharField(max_length = 50)
                  
    def __str__(self):
        return self.hotelname

# class Resortbooking(models.Model):
#     Resortname=models.CharField(max_length = 50)
#     Checkindate =models.CharField(max_length = 50)
#     Checkoutdate = models.CharField(max_length = 50)
#     Createddate = models.CharField(max_length = 50)
      
#     login=models.ForeignKey(log, on_delete=models.CASCADE)

    
#     def __str__(self):
#         return self.Resortname

# class Restaurentbooking(models.Model):
#     Restaurentname=models.CharField(max_length = 50)
#     Bookingdate =models.CharField(max_length = 50)
#     Createddate = models.CharField(max_length = 50)
      
#     login=models.ForeignKey(log, on_delete=models.CASCADE)

    
#     def __str__(self):
#         return self.Restaurentname

# class Travelsbooking(models.Model):
#     Travelsname=models.CharField(max_length = 50)
#     Tripdate =models.CharField(max_length = 50)
#     Createddate = models.CharField(max_length = 50)
#     Amount = models.CharField(max_length = 50)
      
#     login=models.ForeignKey(log, on_delete=models.CASCADE)

    
#     def __str__(self):
#         return self.Travelsname

# class Payment(models.Model):
#     Amount=models.CharField(max_length = 50)
#     Paymentstatus =models.CharField(max_length = 50)
#     Paymentdate = models.CharField(max_length = 50)
    
      
#     login=models.ForeignKey(log, on_delete=models.CASCADE)

    
#     def __str__(self):
#         return self.Amount



# class Reels(models.Model):
#     Footagelength=models.CharField(max_length = 50)
#     Description =models.CharField(max_length = 50)
#     Spotname = models.CharField(max_length = 50)
#     Uploaddate = models.CharField(max_length = 50)
    

    
      
#     login=models.ForeignKey(log, on_delete=models.CASCADE)

    
#     def __str__(self):
#         return self.Footagelength

