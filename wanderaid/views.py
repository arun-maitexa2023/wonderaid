from django.shortcuts import render,redirect
from travelaid.models import user,Hotel,Restaurent,Resort,Travels,Guide,log

# Create your views here.

def index(request):
    return render(request,'index.html')


 #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   






# def reject_Restaurents(request):
#     return render(request,'Requested-Restaurents.html')


def Approved_Resorts(request):
    return render(request,'Approved-Resorts.html')
def Approved_Travels(request):
    return render(request,'Approved-Travels.html')
def Approved_Guides(request):
    return render(request,'Approved-Guides.html')

def Requested_Resorts(request):
    return render(request,'Requested-Resorts.html')
def Requested_Travels(request):
    return render(request,'Requested-Travels.html')
def Requested_Guides(request):
    return render(request,'Requested-Guides.html')
def view_users(request):
    return render(request,'view-users.html')
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

####################################################


def view_users(request):
    data = user.objects.all()
    return render(request,'view-users.html',{'data':data})

#hotel

def Requested_Hotels(request):
    data = Hotel.objects.all()
    return render(request,'Requested-Hotels.html',{'data':data})

def admin_approve_hotel(request, id):
    userdata = Hotel.objects.get(id=id)
    userdata.hotelstatus = 1  #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    userdata.save()
    return redirect('Approved_Hotels')


def admin_reject_hotel(request,id):
    delhotel = hotel.objects.get(id=id)
    print(delhotel.login_id)
    l_id = delhotel.log_id
    print(l_id)
    data = log.objects.get(id+l_id)
    data.delete()
    return redirect('Requested_Hotels')

def Approved_Hotels(request):
    data = Hotel.objects.all()#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    return render(request,'Approved-Hotels.html',{'data':data})


# resturant


def Requested_Restaurents(request):
    data = Restaurent.objects.all()
    return render(request,'Requested-Restaurents.html',{'data':data})

def Approved_Restaurents(request):
    data = Restaurent.objects.all()
    return render(request,'Approved-Restaurents.html',{'data':data})

def admin_approve_Restaurents(request, id):
    userdata = Restaurent.objects.get(id=id)
    userdata.Restaurentstatus = 1  
    userdata.save()
    return redirect('Approved_Restaurents')


def admin_reject_Restaurents(request,id):
    delRestaurents = Restaurents.objects.get(id=id)
    print(delRestaurents.login_id)
    l_id = delRestaurents.log_id
    print(l_id)
    data = log.objects.get(id+l_id)
    data.delete()
    return redirect('Requested_Restaurents')


#resort


def Requested_Resorts(request):
    data = Resort.objects.all()
    return render(request,'Requested-Resorts.html',{'data':data})

def Approved_Resorts(request):
    data = Resort.objects.all()
    return render(request,'Approved-Resorts.html',{'data':data})

def admin_approve_Resorts(request, id):
    userdata = Resort.objects.get(id=id)
    userdata.resortstatus = 1  
    userdata.save()
    return redirect('Approved_Resorts')


def admin_reject_Resorts(request,id):
    delResorts = Resort.objects.get(id=id)
    print(delResort.login_id)
    l_id = delResort.log_id
    print(l_id)
    data = log.objects.get(id+l_id)
    data.delete()
    return redirect('Requested_Resorts')


#Travelse

def Requested_Travels(request):
    data = Travels.objects.all()
    return render(request,'Requested-Travels.html',{'data':data})

def Approved_Travels(request):
    data = Travels.objects.all()
    return render(request,'Approved-Travels.html',{'data':data})

def admin_approve_Travels(request, id):
    userdata = Travels.objects.get(id=id)
    userdata.travelsstatus = 1  
    userdata.save()
    return redirect('Approved_Travels')


def admin_reject_Travels(request,id):
    delTravels = Travels.objects.get(id=id)
    print(delTravels.login_id)
    l_id = delTravels.log_id
    print(l_id)
    data = log.objects.get(id+l_id)
    data.delete()
    return redirect('Requested_Travels')

#Guides

def Requested_Guide(request):
    data = Guide.objects.all()
    return render(request,'Requested-Guides.html',{'data':data})

def Approved_Guide(request):
    data = Guide.objects.all()
    return render(request,'Approved-Guides.html',{'data':data})

def admin_approve_Guide(request, id):
    userdata = Guide.objects.get(id=id)
    userdata.Guidesstatus = 1  
    userdata.save()
    return redirect('Approved_Guide')


def admin_reject_Guide(request,id):
    delGuide = Guide.objects.get(id=id)
    print(delGuide.login_id)
    l_id = delGuide.log_id
    print(l_id)
    data = log.objects.get(id+l_id)
    data.delete()
    return redirect('Requested_Guide')
