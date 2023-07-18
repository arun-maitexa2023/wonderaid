from django.shortcuts import render,redirect
from .serializers import loginUsersSerializer,UserRegisterSerializer,HotelRegisterSerializer,RestaurentRegisterSerializer,ResortRegisterSerializer,TravelsRegisterSerializer,GuideRegisterSerializer,SpotsSerializer,UserprofileSerializer,PlannedtripSerializer,CommentsSerializer,NotificationSerializer,PackegeHotelSerializer,PackegeResortSerializer,PackegeTravelsSerializer,ChatcommunitySerializer,ReelsSerializer,ResortbookingSerializer,HotelbookingSerializer
from .models import log, user, Hotel, Restaurent, Resort, Travels, Guide,Spots,Userprofile,Plannedtrip,Comments,Notification,PackegeHotel,PackegeResort,PackegeTravels,Chatcommunity,Reels,Resortbooking,Hotelbooking
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView

#Create your views here.

class userRegisterAPIView(GenericAPIView):
    serializer_class = UserRegisterSerializer
    serializer_class_login = loginUsersSerializer 
    def post(self,request):

        login_id=''
        name = request.data.get("name")
        email = request.data.get('useremail')
        dob =request.data.get('userdob')
        gender = request.data.get('usergender')
        place= request.data.get('userplace')
        pincode = request.data.get('userpincode')
        phone = request.data.get('userphone')
        username = request.data.get('username')
        password = request.data.get('userpassword')
        dp = request.data.get('userdp')

        userstatus="1"
        role="user"
        
        if(log.objects.filter(username=name)):
            return Response({'message' : 'Duplicate Username Found'},status.HTTP_400_BAD_REQUEST)
        else:
            serializer_login = self.serializer_class_login(data={'username': name,'password': password,'role':role})

        if serializer_login.is_valid():
            Log = serializer_login.save()
            login_id = Log.id
            print(login_id)
        serializer = self.serializer_class(
            data = {
                'name':name,
                'usermail':email,
                'userplace':place,
                'usergender':gender,
                'userdob':dob,
                'userphone':phone,
                'usermail':email,
                'userpincode':pincode,
                'userdp':dp,
                'userpassword':password,
                'role':role,
                'userstatus':userstatus,
                'login':login_id,
            }
            
            )

        print(serializer)
        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({'data':serializer.data,'message':'Registration Succesful','success':True},status =status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':' Registration Failed','success':False},status=status.HTTP_400_BAD_REQUEST)



class HotelRegisterAPIView(GenericAPIView):
    serializer_class = HotelRegisterSerializer
    serilalizer_class_login = loginUsersSerializer
    def post(self,request):
        login_id=''
        htlname = request.data.get("hotelname")
        htlmail = request.data.get("hotelmail")
        htllocation = request.data.get('hotellocation')
        htlpincode =request.data.get('hotelpincode')
        htlphone = request.data.get('hotelphone')
        htlplace= request.data.get('hotelrating')
        htlrooms = request.data.get('hotelrooms')
        htlcategory = request.data.get('hotelcategory')
        htlmenu = request.data.get('menu')
        htlreviews = request.data.get('reviews')
        htlfecilities = request.data.get('hotelfecilities')
        htlpackages = request.data.get('hotelpackages')
        htlservices = request.data.get('hotelservices')
        htltiming = request.data.get('hoteltiming')
        htlspoffers = request.data.get('specialoffers')
        htlavailability = request.data.get('roomsavailability')
        htldesc = request.data.get('description')
        htlnba = request.data.get('nba')
        htlpolicies = request.data.get('policies')
        htlpassword = request.data.get('hotelpass')
        htlimg = request.data.get('images')
        htlstatus="0"
        role="hotel"
        
        if(log.objects.filter(username=htlname)):
            return Response({'message' : 'Duplicate Username Found'},status.HTTP_400_BAD_REQUEST)
        else:
            serializer_login = self.serilalizer_class_login(data={'username': htlname,'password': htlpassword,'role':role})

        if serializer_login.is_valid():
            Log = serializer_login.save()
            login_id = Log.id
            print(login_id)
        serializer = self.serializer_class(
            data = {
                    'hotelname': htlname,
                    'hotelmail': htlmail,
                    'hotellocation': htllocation,
                    'hotelpincode': htlpincode,
                    'hotelphone': htlphone,
                    'hotelplace': htlplace,
                    'hotelrooms': htlrooms,
                    'hotelcategory': htlcategory,
                    'menu': htlmenu,
                    'reviews': htlreviews,
                    'hotelfecilities': htlfecilities,
                    'hotelpackages': htlpackages,
                    'hotelservices': htlservices,
                    'hoteltiming': htltiming,
                    'specialoffers': htlspoffers,
                    'availability': htlavailability,
                    'description': htldesc,
                    'nba': htlnba,
                    'policies': htlpolicies,
                    'hotelpass': htlpassword,
                    'image': htlimg,
                    'hotelstatus': htlstatus,
                    'login':login_id,
                    'role': role,
                    'login':login_id,
                }
                
                )
        print(serializer)
        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({'data':serializer.data,'message':'Registration Succesful','success':True},status =status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':' Registration Failed','success':False},status=status.HTTP_400_BAD_REQUEST)



class RestaurentRegisterAPIView(GenericAPIView):
    serializer_class = RestaurentRegisterSerializer
    serializer_class_login = loginUsersSerializer
    def post(self,request):
        login_id=''
        rstrntname = request.data.get("restaurentname")
        rstrntmail = request.data.get("restaurentmail")
        rstrntlocation = request.data.get('restaurentlocation')
        rstrntpincode =request.data.get('restaurentpin')
        rstrntphone = request.data.get('restaurentphone')
        rstrntrating= request.data.get('restaurentrating')
        rstrntcategory = request.data.get('restaurentcategory')
        rstrnttiming = request.data.get('restaurenttiming')
        rstrntspoffers = request.data.get('specialoffers')
        rstrntspcls = request.data.get('specials')
        rstrntdesc = request.data.get('description')
        rstrntnba = request.data.get('nba')
        rstrntpolicies = request.data.get('policies')
        rstrntmenu= request.data.get('restaurentmenu')
        rstrntdiningopt= request.data.get('diningoptions')
        rstrntreviews = request.data.get('reviews')
        rstrntpassword = request.data.get('restaurentpass')
        rstrntimg = request.data.get('images')
        rstrntstatus="0"
        role="resort"
        
        if(log.objects.filter(username=rstrntname)):
            return Response({'message' : 'Duplicate Username Found'},status.HTTP_400_BAD_REQUEST)
        else:
            serializer_login = self.serializer_class_login(data={'username': rstrntname,'password': rstrntpassword,'role':role})

        if serializer_login.is_valid():
            Log = serializer_login.save()
            login_id = Log.id
            print(login_id)
        serializer = self.serializer_class(
            data = {
                    'restaurentname': rstrntname,
                    'restaurentmail': rstrntmail,
                    'restaurentlocation': rstrntlocation,
                    'restaurentpin': rstrntpincode,
                    'restaurentphone': rstrntphone,
                    'restaurentrating': rstrntrating,
                    'restaurentcategory': rstrntcategory,
                    'restaurentmenu': rstrntmenu,
                    'reviews': rstrntreviews,
                    'restaurenttiming': rstrnttiming,
                    'specialoffers': rstrntspoffers,
                    'specials' :rstrntspcls,
                    'diningoptions' :rstrntdiningopt,
                    'description': rstrntdesc,
                    'nba': rstrntnba,
                    'policies': rstrntpolicies,
                    'restaurentpass': rstrntpassword,
                    'images': rstrntimg,
                    'Restaurentstatus': rstrntstatus,
                    'login':login_id,
                    'role': role,
                }
                
                )
        print(serializer)
        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({'data':serializer.data,'message':'Registration Succesful','success':True},status =status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':' Registration Failed','success':False},status=status.HTTP_400_BAD_REQUEST)



class ResortRegisterAPIView(GenericAPIView):
    serializer_class = ResortRegisterSerializer
    serializer_class_login = loginUsersSerializer
    def post(self,request):
        login_id=''
        rstname = request.data.get("resortname")
        rstmail = request.data.get("resortmail")
        rstlocation = request.data.get('resortlocation')
        rstpincode =request.data.get('resortpincode')
        rstphone = request.data.get('resortphone')
        rstrating= request.data.get('resortrating')
        rstrooms = request.data.get('resortrooms')
        rstcategory = request.data.get('resortcategory')
        rstfecilities = request.data.get('resortfecilities')
        rstpackages = request.data.get('resortpackages')
        rstservices = request.data.get('resortservices')
        rsttiming = request.data.get('resorttiming')
        rstspoffers = request.data.get('specialoffers')
        rstavailability = request.data.get('availability')
        rstdesc = request.data.get('description')
        rstnba = request.data.get('nba')
        rstpolicies = request.data.get('policies')
        rstacctypes= request.data.get('accomodationtypes')
        rstaccdesc= request.data.get('accomodationdesc')
        rstfdmenu= request.data.get('foodmenu')
        rstdiningopt= request.data.get('diningoptions')
        rstpricing= request.data.get('pricing')
        rstreviews= request.data.get('reviews')
        rstpassword = request.data.get('resortpass')
        rstimg = request.data.get('images')
        rststatus="0"
        role="resort"
        
        if(log.objects.filter(username=rstname)):
            return Response({'message' : 'Duplicate Username Found'},status.HTTP_400_BAD_REQUEST)
        else:
            serializer_login = self.serializer_class_login(data={'username': rstname,'password': rstpassword,'role':role})

        if serializer_login.is_valid():
            Log = serializer_login.save()
            login_id = Log.id
            print(login_id)
        serializer = self.serializer_class(
            data = {
                    'resortname': rstname,
                    'resortmail': rstmail,
                    'resortlocation': rstlocation,
                    'resortpincode': rstpincode,
                    'resortphone': rstphone,
                    'resortrating': rstrating,
                    'resortrooms': rstrooms,
                    'resortcategory': rstcategory,
                    'accomodationtypes':rstacctypes,
                    'accomodationdesc':rstaccdesc,
                    'foodmenu': rstfdmenu,
                    'diningoptions':rstdiningopt,
                    'pricing':rstpricing,
                    'reviews': rstreviews,
                    'resortfecilities': rstfecilities,
                    'resortpackages': rstpackages,
                    'resortservices': rstservices,
                    'resorttiming': rsttiming,
                    'specialoffers': rstspoffers,
                    'availability': rstavailability,
                    'description': rstdesc,
                    'nba': rstnba,
                    'policies': rstpolicies,
                    'resortpass': rstpassword,
                    'image': rstimg,
                    'resortstatus': rststatus,
                    'login':login_id,
                    'role': role
                }
                
                )
        print(serializer)
        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({'data':serializer.data,'message':'Registration Succesful','success':True},status =status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':' Registration Failed','success':False},status=status.HTTP_400_BAD_REQUEST)


class TravelsRegisterAPIView(GenericAPIView):
    serializer_class = TravelsRegisterSerializer
    serializer_class_login = loginUsersSerializer
    def post(self,request):
        login_id=''
        trvlsname = request.data.get("travelsname")
        trvlsmail = request.data.get("travelsmail")
        trvlslocation = request.data.get('travelslocation')
        trvlspincode =request.data.get('travelspincode')
        trvlsphone = request.data.get('travelsphone')
        trvlsrating= request.data.get('travelsrating')
        trvlspackages = request.data.get('travelspackages')
        trvlstiming = request.data.get('travelstiming')
        trvlspolicies = request.data.get('policies')
        trvlsreviews= request.data.get('reviews')
        trvlspassword = request.data.get('travelspass')
        trvlsimg = request.data.get('images')
        trvlsstatus="0"
        role="travels"
        
        if(log.objects.filter(username=trvlsname)):
            return Response({'message' : 'Duplicate Username Found'},status.HTTP_400_BAD_REQUEST)
        else:
            serializer_login = self.serializer_class_login(data={'username': trvlsname,'password': trvlspassword,'role':role})

        if serializer_login.is_valid():
            Log = serializer_login.save()
            login_id = Log.id
            print(login_id)
        serializer = self.serializer_class(
            data = {
                    'travelsname': trvlsname,
                    'travelsmail': trvlsmail,
                    'travelslocation': trvlslocation,
                    'travelspincode': trvlspincode,
                    'travelsphone': trvlsphone,
                    'travelsrating': trvlsrating,
                    'reviews': trvlsreviews,
                    'travelspackages': trvlspackages,
                    'travelstiming': trvlstiming,
                    'policies': trvlspolicies,
                    'reviews':trvlsreviews,
                    'travelspass': trvlspassword,
                    'image': trvlsimg,
                    'travelsstatus': trvlsstatus,
                    'login':login_id,
                    'role': role
                }
                )
        print(serializer)
        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({'data':serializer.data,'message':'Registration Succesful','success':True},status =status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':' Registration Failed','success':False},status=status.HTTP_400_BAD_REQUEST)

class GuideRegisterAPIView(GenericAPIView):
    serializer_class = GuideRegisterSerializer
    serializer_class_login = loginUsersSerializer
    def post(self,request):
        login_id=''
        gdname = request.data.get("guidename")
        gdmail = request.data.get("guidemail")
        gdlocation = request.data.get('guidelocation')
        gdpincode =request.data.get('guidepincode')
        gdphone = request.data.get('guidephone')
        gdrating= request.data.get('guiderating')
        gdreviews= request.data.get('guidereviews')
        gdpassword = request.data.get('guiderepass')
        gddp = request.data.get('guidedp')
        gdstatus="0"
        role="guide"
        
        if(log.objects.filter(username=gdname)):
            return Response({'message' : 'Duplicate Username Found'},status.HTTP_400_BAD_REQUEST)
        else:
            serializer_login = self.serializer_class_login(data={'username': gdname,'password': gdpassword,'role':role})

        if serializer_login.is_valid():
            Log = serializer_login.save()
            login_id = Log.id
            print(login_id)
        serializer = self.serializer_class(
            data = {
                    'guidename': gdname,
                    'guidemail': gdmail,
                    'guidelocation': gdlocation,
                    'guidepincode': gdpincode,
                    'guidephone': gdphone,
                    'guiderating': gdrating,
                    'reviews': gdreviews,
                    'guiderepass': gdpassword,
                    'guidedp': gddp,
                    'Guidesstatus': gdstatus,
                    'login':login_id,
                    'role': role
                }
                )
        print(serializer)
        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({'data':serializer.data,'message':'Registration Succesful','success':True},status =status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':' Registration Failed','success':False},status=status.HTTP_400_BAD_REQUEST)

#         #login

class LoginAPIView(GenericAPIView):
    serializer_class = loginUsersSerializer

    def post (self,request):
        u_id= ''
        username = request.data.get('username')
        password = request.data.get('password')
        print(username)
        print(password)
        logreg=log.objects.filter(username=username,password=password)
        #print(logreg)
       # print(logreg.count)
        if(logreg.count()>0):
            read_serializer = loginUsersSerializer(logreg, many=True)
            for i in read_serializer.data:
                id=i['id']
                print(id)
                role = i['role']
                regdata = user.objects.all().filter(login = id).values()
                print(regdata)

                for i in regdata:
                    u_id = i['id']
                    name = i['name']
                    l_status=i['userstatus']
                    print(u_id)
                regdata=Hotel.objects.all().filter(login=id).values()
                print(regdata)
                for i in regdata:
                    u_id = i['id']
                    name = i['hotelname']
                    l_status =i['hotelstatus']
                    print(l_status)
                    print(u_id)

                regdata = Restaurent.objects.all().filter(login = id).values()
                print(regdata)

                for i in regdata:
                    u_id = i['id']
                    name = i['restaurentname']
                    l_status=i['Restaurentstatus']
                    print(u_id)
                regdata=Resort.objects.all().filter(login=id).values()
                print(regdata)
                for i in regdata:
                    u_id = i['id']
                    name = i['resortname']
                    l_status =i['resortstatus']
                    print(l_status)
                    print(u_id)

                regdata = Travels.objects.all().filter(login = id).values()
                print(regdata)

                for i in regdata:
                    u_id = i['id']
                    name = i['travelsname']
                    l_status=i['travelsstatus']
                    print(u_id)

                regdata=Guide.objects.all().filter(login=id).values()
                print(regdata)
                for i in regdata:
                    u_id = i['id']
                    name = i['guidename']
                    l_status =i['Guidesstatus']
                    print(l_status)
                    print(u_id)

            return Response({
                'data':{
                    'login_id':id,
                    'username':username,
                    'password':password,
                    'role':role,
                    'userid':u_id,
                    'status':l_status
                },
                'success':True,
                'message':'Logged In Successfully'
            },status=status.HTTP_200_OK)
        else:
            return Response({
                'message':'username is invalid',
                'success':False
                },status = status.HTTP_400_BAD_REQUEST)
        
# view all users 

class Get_All_UsersAPIView(GenericAPIView):
    serializer_class = UserRegisterSerializer
    def get(self,request):
        queryset = user.objects.all()
        if(queryset.count()>0):
            serializer = UserRegisterSerializer(queryset,many= True)
   

            return Response({'data':serializer.data,'message':'all user data set','success' : True},status = status.HTTP_200_OK)
        else:
    
            return Response({'data':'non data available','success':False},status = status.HTTP_201_CREATED)


#single user view

class Get_single_UserAPIView(GenericAPIView):
    def get(self,request,id):
        queryset = user.objects.get(pk=id)
        serializer =UserRegisterSerializer(queryset)
        return Response({'data':serializer.data,'message':'single user data','success':True},status =status.HTTP_200_OK)


#update user

class Update_UserAPIView(GenericAPIView):
    serializer_class=UserRegisterSerializer
    def put(self,request,id):
        queryset = user.objects.get(pk=id)
        print(queryset)
        serializer = UserRegisterSerializer(instance = queryset,data=request.data,partial= True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'updated succesfully','success':True},status = status.HTTP_200_OK)
        else:
            return Response({'data':'something went wrong','success': False},status = status.HTTP_400_BAD_REQUEST)
#Delete User
class Delete_userAPIView(GenericAPIView):
    def delete(self, request, log_id):
        delmember = log.objects.get(pk=log_id)
        delmember.delete()
        return Response({'message':'Deleted successfully', 'success':True}, status=status.HTTP_200_OK)


# view all hotels 

class Get_All_HotelsAPIView(GenericAPIView):
    serializer_class = HotelRegisterSerializer
    def get(self,request):
        queryset = Hotel.objects.all()
        if(queryset.count()>0):
            serializer = HotelRegisterSerializer(queryset,many= True)
   

            return Response({'data':serializer.data,'message':'all hotel data set','success' : True},status = status.HTTP_200_OK)
        else:    
            return Response({'data':'non data available','success':False},status = status.HTTP_201_CREATED)


#single hotel view

class Get_single_HotelAPIView(GenericAPIView):
    def get(self,request,id):
        queryset = Hotel.objects.get(pk=id)
        serializer =HotelRegisterSerializer(queryset)
        return Response({'data':serializer.data,'message':'single hotel data','success':True},status =status.HTTP_200_OK)

#update hotel

class Update_HotelAPIView(GenericAPIView):
    serializer_class=HotelRegisterSerializer
    def put(self,request,id):
        queryset = Hotel.objects.get(pk=id)
        print(queryset)
        serializer = HotelRegisterSerializer(instance = queryset,data=request.data,partial= True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'updated succesfully','success':True},status = status.HTTP_200_OK)
        else:
            return Response({'data':'something went wrong','success': False},status = status.HTTP_400_BAD_REQUEST)



# view all Restaurents 

class Get_All_RestaurentsAPIView(GenericAPIView):
    serializer_class = RestaurentRegisterSerializer
    def get(self,request):
        queryset = Restaurent.objects.all()
        if(queryset.count()>0):
            serializer = RestaurentRegisterSerializer(queryset,many= True)
   

            return Response({'data':serializer.data,'message':'all Restaurent data set','success' : True},status = status.HTTP_200_OK)
        else:    
            return Response({'data':'non data available','success':False},status = status.HTTP_201_CREATED)


#single Restaurent view

class Get_single_RestaurentAPIView(GenericAPIView):
    def get(self,request,id):
        queryset = Restaurent.objects.get(pk=id)
        serializer =RestaurentRegisterSerializer(queryset)
        return Response({'data':serializer.data,'message':'single Restaurent data','success':True},status =status.HTTP_200_OK)

#update Restaurent

class Update_RestaurentAPIView(GenericAPIView):
    serializer_class=RestaurentRegisterSerializer
    def put(self,request,id):
        queryset = Restaurent.objects.get(pk=id)
        print(queryset)
        serializer = RestaurentRegisterSerializer(instance = queryset,data=request.data,partial= True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'updated succesfully','success':True},status = status.HTTP_200_OK)
        else:
            return Response({'data':'something went wrong','success': False},status = status.HTTP_400_BAD_REQUEST)





# view all Resorts 

class Get_All_ResortsAPIView(GenericAPIView):
    serializer_class = ResortRegisterSerializer
    def get(self,request):
        queryset = Resort.objects.all()
        if(queryset.count()>0):
            serializer = ResortRegisterSerializer(queryset,many= True)
   

            return Response({'data':serializer.data,'message':'all Resort data set','success' : True},status = status.HTTP_200_OK)
        else:    
            return Response({'data':'non data available','success':False},status = status.HTTP_201_CREATED)


#single Resort view

class Get_single_ResortAPIView(GenericAPIView):
    def get(self,request,id):
        queryset = Resort.objects.get(pk=id)
        serializer =ResortRegisterSerializer(queryset)
        return Response({'data':serializer.data,'message':'single Resort data','success':True},status =status.HTTP_200_OK)

#update Resort

class Update_ResortAPIView(GenericAPIView):
    serializer_class=ResortRegisterSerializer
    def put(self,request,id):
        queryset = Resort.objects.get(pk=id)
        print(queryset)
        serializer = ResortRegisterSerializer(instance = queryset,data=request.data,partial= True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'updated succesfully','success':True},status = status.HTTP_200_OK)
        else:
            return Response({'data':'something went wrong','success': False},status = status.HTTP_400_BAD_REQUEST)



# view all Travels 

class Get_All_TravelsAPIView(GenericAPIView):
    serializer_class = TravelsRegisterSerializer
    def get(self,request):
        queryset = Travels.objects.all()
        if(queryset.count()>0):
            serializer = TravelsRegisterSerializer(queryset,many= True)
   

            return Response({'data':serializer.data,'message':'all Travels data set','success' : True},status = status.HTTP_200_OK)
        else:    
            return Response({'data':'non data available','success':False},status = status.HTTP_201_CREATED)


#single Travels view

class Get_single_TravelsAPIView(GenericAPIView):
    def get(self,request,id):
        queryset = Travels.objects.get(pk=id)
        serializer =TravelsRegisterSerializer(queryset)
        return Response({'data':serializer.data,'message':'single Travels data','success':True},status =status.HTTP_200_OK)

#update Travels

class Update_TravelsAPIView(GenericAPIView):
    serializer_class=TravelsRegisterSerializer
    def put(self,request,id):
        queryset = Travels.objects.get(pk=id)
        print(queryset)
        serializer = TravelsRegisterSerializer(instance = queryset,data=request.data,partial= True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'updated succesfully','success':True},status = status.HTTP_200_OK)
        else:
            return Response({'data':'something went wrong','success': False},status = status.HTTP_400_BAD_REQUEST)



# view all Guides 

class Get_All_GuidesAPIView(GenericAPIView):
    serializer_class = GuideRegisterSerializer
    def get(self,request):
        queryset = Guide.objects.all()
        if(queryset.count()>0):
            serializer = GuideRegisterSerializer(queryset,many= True)
   

            return Response({'data':serializer.data,'message':'all Guide data set','success' : True},status = status.HTTP_200_OK)
        else:    
            return Response({'data':'non data available','success':False},status = status.HTTP_201_CREATED)


#single Guide view

class Get_single_GuideAPIView(GenericAPIView):
    def get(self,request,id):
        queryset = Guide.objects.get(pk=id)
        serializer =GuideRegisterSerializer(queryset)
        return Response({'data':serializer.data,'message':'single Guide data','success':True},status =status.HTTP_200_OK)

#update Guide

class Update_GuideAPIView(GenericAPIView):
    serializer_class=GuideRegisterSerializer
    def put(self,request,id):
        queryset = Guide.objects.get(pk=id)
        print(queryset)
        serializer = GuideRegisterSerializer(instance = queryset,data=request.data,partial= True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'updated succesfully','success':True},status = status.HTTP_200_OK)
        else:
            return Response({'data':'something went wrong','success': False},status = status.HTTP_400_BAD_REQUEST)



#Add more details of user table

class Moredetails_of_User_APIView(GenericAPIView):

    serializer_class = UserRegisterSerializer

    def post(self, request, id):
        fullname = request.data.get('fullname')
        userdob = request.data.get('userdob')
        usergender = request.data.get('usergender')
        userplace = request.data.get('userplace')
        userpincode = request.data.get('userpincode')
        userdp = request.data.get('userdp')


        if id:
            userdata = user.objects.get(id=id)
            userdata.fullname = fullname
            userdata.userdob = userdob
            userdata.usergender = usergender
            userdata.userplace = userplace
            userdata.userpincode = userpincode
            userdata.userdp = userdp
            userdata.save()

            serializer = self.serializer_class(userdata)
            return Response({'data': serializer.data, 'message': 'user data updated successfully', 'success': True}, status=status.HTTP_201_CREATED)

        return Response({'message': 'Invalid request', 'success': False}, status=status.HTTP_400_BAD_REQUEST)


#Add more details of Hotel table

class Moredetails_of_Hotel_APIView(GenericAPIView):

    serializer_class = HotelRegisterSerializer

    def post(self, request, id):
        hotellocation = request.data.get('hotellocation')
        hotelpincode = request.data.get('hotelpincode')
        hotelrating = request.data.get('hotelrating')
        hotelrooms = request.data.get('hotelrooms')
        hotelcategory = request.data.get('hotelcategory')
        hotelfecilities = request.data.get('hotelfecilities')
        hotelpackages = request.data.get('hotelpackages')
        hotelservices = request.data.get('hotelservices')
        hoteltiming = request.data.get('hoteltiming')
        specialoffers = request.data.get('specialoffers')
        roomsavailability = request.data.get('roomsavailability')
        description = request.data.get('description')
        nba = request.data.get('nba')
        policies = request.data.get('policies')
        menu = request.data.get('menu')
        reviews = request.data.get('reviews')
        images = request.data.get('images')



        if id:
            Hoteldata = Hotel.objects.get(id=id)
            Hoteldata.hotellocation = hotellocation
            Hoteldata.hotelpincode = hotelpincode
            Hoteldata.hotelrating = hotelrating
            Hoteldata.hotelrooms = hotelrooms
            Hoteldata.hotelcategory = hotelcategory
            Hoteldata.hotelfecilities = hotelfecilities
            Hoteldata.hotelpackages = hotelpackages
            Hoteldata.hotelservices = hotelservices
            Hoteldata.hoteltiming = hoteltiming
            Hoteldata.specialoffers = specialoffers
            Hoteldata.roomsavailability = roomsavailability
            Hoteldata.description = description
            Hoteldata.nba = nba
            Hoteldata.policies = policies
            Hoteldata.menu =menu
            Hoteldata.reviews = reviews
            Hoteldata.images = images
            Hoteldata.save()

            serializer = self.serializer_class(Hoteldata)
            return Response({'data': serializer.data, 'message': 'Hotel data updated successfully', 'success': True}, status=status.HTTP_201_CREATED)

        return Response({'message': 'Invalid request', 'success': False}, status=status.HTTP_400_BAD_REQUEST)


#Add more details of Restaurent table

class Moredetails_of_Restaurent_APIView(GenericAPIView):

    serializer_class = RestaurentRegisterSerializer

    def post(self, request, id):
        restaurentlocation = request.data.get('restaurentlocation')
        restaurentpin = request.data.get('restaurentpin')
        restaurentrating = request.data.get('restaurentrating')
        restaurentcategory = request.data.get('restaurentcategory')
        restaurentmenu = request.data.get('restaurentmenu')
        specialoffers = request.data.get('specialoffers')
        specials = request.data.get('specials')
        description = request.data.get('description')
        nba = request.data.get('nba')
        policies = request.data.get('policies')
        diningoptions = request.data.get('diningoptions')
        restaurenttiming = request.data.get('restaurenttiming')
        reviews = request.data.get('reviews')
        images = request.data.get('images')
        # images = request.data.get('images')



        if id:
            Restaurentdata = Restaurent.objects.get(id=id)
            Restaurentdata.restaurentlocation = restaurentlocation
            Restaurentdata.restaurentpin = restaurentpin
            Restaurentdata.restaurentrating = restaurentrating
            Restaurentdata.restaurentcategory = restaurentcategory
            Restaurentdata.restaurentmenu = restaurentmenu
            Restaurentdata.specialoffers = specialoffers
            Restaurentdata.specials = specials
            Restaurentdata.description = description
            Restaurentdata.nba = nba
            Restaurentdata.policies = policies
            Restaurentdata.diningoptions = diningoptions
            Restaurentdata.restaurenttiming = restaurenttiming
            Restaurentdata.reviews = reviews
            Restaurentdata.images = images
           
            
            Restaurentdata.save()

            serializer = self.serializer_class(Restaurentdata)
            return Response({'data': serializer.data, 'message': 'Restaurent data updated successfully', 'success': True}, status=status.HTTP_201_CREATED)

        return Response({'message': 'Invalid request', 'success': False}, status=status.HTTP_400_BAD_REQUEST)


#Add more details of Resort table

class Moredetails_of_Resort_APIView(GenericAPIView):

    serializer_class = ResortRegisterSerializer

    def post(self, request, id):
        resortlocation = request.data.get('resortlocation')
        resortpincode = request.data.get('resortpincode')
        resortrating = request.data.get('resortrating')
        resortrooms = request.data.get('resortrooms')
        resortcategory = request.data.get('resortcategory')
        resortpackages = request.data.get('resortpackages')
        resortservices = request.data.get('resortservices')
        resortfecilities = request.data.get('resortfecilities')
        resorttiming = request.data.get('resorttiming')
        specialoffers = request.data.get('specialoffers')
        availability = request.data.get('availability')
        description = request.data.get('description')
        nba = request.data.get('nba')
        policies = request.data.get('policies')
        accomodationtypes = request.data.get('accomodationtypes')
        accomodationdesc = request.data.get('accomodationdesc')
        foodmenu = request.data.get('foodmenu')
        diningoptions = request.data.get('diningoptions')
        pricing = request.data.get('pricing')
        reviews = request.data.get('reviews')
        images = request.data.get('images')
        
     



        if id:
            Resortdata = Resort.objects.get(id=id)
            Resortdata.resortlocation = resortlocation
            Resortdata.resortpincode = resortpincode
            Resortdata.resortrating = resortrating
            Resortdata.resortrooms = resortrooms
            Resortdata.resortcategory = resortcategory
            Resortdata.resortpackages = resortpackages
            Resortdata.resortservices = resortservices
            Resortdata.resortfecilities = resortfecilities
            Resortdata.resorttiming = resorttiming
            Resortdata.specialoffers = specialoffers
            Resortdata.availability = availability
            Resortdata.description = description
            Resortdata.nba = nba
            Resortdata.policies = policies
            Resortdata.accomodationtypes = accomodationtypes
            Resortdata.accomodationdesc = accomodationdesc
            Resortdata.foodmenu = foodmenu
            Resortdata.diningoptions = diningoptions
            Resortdata.pricing = pricing
            Resortdata.reviews = reviews
            Resortdata.images = images
    
           
            
            Resortdata.save()

            serializer = self.serializer_class(Resortdata)
            return Response({'data': serializer.data, 'message': 'Resort data updated successfully', 'success': True}, status=status.HTTP_201_CREATED)

        return Response({'message': 'Invalid request', 'success': False}, status=status.HTTP_400_BAD_REQUEST)


#Add more details of Travels table

class Moredetails_of_Travels_APIView(GenericAPIView):

    serializer_class = TravelsRegisterSerializer

    def post(self, request, id):
        travelslocation = request.data.get('travelslocation')
        travelspincode = request.data.get('travelspincode')
        travelsrating = request.data.get('travelsrating')
        travelspackages = request.data.get('travelspackages')
        travelstiming = request.data.get('travelstiming')
        policies = request.data.get('policies')
        reviews = request.data.get('reviews')
        images = request.data.get('images') 



        if id:
            Travelsdata = Travels.objects.get(id=id)
            Travelsdata.travelslocation = travelslocation
            Travelsdata.travelspincode = travelspincode
            Travelsdata.travelsrating = travelsrating
            Travelsdata.travelspackages = travelspackages
            Travelsdata.travelstiming = travelstiming
            Travelsdata.policies = policies
            Travelsdata.reviews = reviews
            Travelsdata.images = images
       
            
            
    
           
            
            Travelsdata.save()

            serializer = self.serializer_class(Travelsdata)
            return Response({'data': serializer.data, 'message': 'Travel data updated successfully', 'success': True}, status=status.HTTP_201_CREATED)

        return Response({'message': 'Invalid request', 'success': False}, status=status.HTTP_400_BAD_REQUEST)

#Add more details of Guide table

class Moredetails_of_Guide_APIView(GenericAPIView):

    serializer_class = GuideRegisterSerializer

    def post(self, request, id):
        guidelocation = request.data.get('guidelocation')
        guidepincode = request.data.get('guidepincode')
        guiderating = request.data.get('guiderating')
        Reviews = request.data.get('Reviews')
        guidedp = request.data.get('guidedp')
    
        if id:
            Guidedata = Guide.objects.get(id=id)
            Guidedata.guidelocation = guidelocation
            Guidedata.guidepincode = guidepincode
            Guidedata.guiderating = guiderating
            Guidedata.Reviews = Reviews
            Guidedata.guidedp = guidedp
              
                     
            
            Guidedata.save()

            serializer = self.serializer_class(Guidedata)
            return Response({'data': serializer.data, 'message': 'Travel data updated successfully', 'success': True}, status=status.HTTP_201_CREATED)

        return Response({'message': 'Invalid request', 'success': False}, status=status.HTTP_400_BAD_REQUEST)

#Hotel search
class HotelsSearchAPIView(GenericAPIView):
    def post(self, request):
        query = request.data.get('query')
        print(query)

        i = Hotel.objects.filter(hotelname__icontains=query) | Hotel.objects.filter(hotellocation__icontains=query)
        for dta in i:
            print(dta)

        data = [{'hotelname': info.hotelname, 'hotelphone': info.hotelphone, 'hotelrating': info.hotelrating, 'hotelcategory': info.hotelcategory,'description': info.description, 'specialoffers': info.specialoffers}
                for info in i]
        return Response({'data': data, 'message': 'Successfully fetched', 'success': True}, status=status.HTTP_200_OK)


#Restaurent search
class RestaurentSearchAPIView(GenericAPIView):
    def post(self, request):
        query = request.data.get('query')
        print(query)

        i = Restaurent.objects.filter(restaurentname__icontains=query) | Restaurent.objects.filter(restaurentlocation__icontains=query)
        for dta in i:
            print(dta)

        data = [{'restaurentname': info.restaurentname, 'restaurentphone': info.restaurentphone, 'restaurentlocation': info.restaurentlocation, 'restaurentpin': info.restaurentpin,'restaurentrating': info.restaurentrating, 'restaurentcategory': info.restaurentcategory}
                for info in i]
        return Response({'data': data, 'message': 'Successfully fetched', 'success': True}, status=status.HTTP_200_OK)


#Resort search
class ResortSearchAPIView(GenericAPIView):
    def post(self, request):
        query = request.data.get('query')
        print(query)

        i = Resort.objects.filter(resortname__icontains=query) | Resort.objects.filter(resortlocation__icontains=query)
        for dta in i:
            print(dta)

        data = [{'resortname': info.resortname, 'resortphone': info.resortphone, 'resortlocation': info.resortlocation, 'resortpincode': info.resortpincode,'restaurentrating': info.resortrating, 'resortrating': info.restaurentcategory}
                for info in i]
        return Response({'data': data, 'message': 'Successfully fetched', 'success': True}, status=status.HTTP_200_OK)


#Travels search
class TravelsSearchAPIView(GenericAPIView):
    def post(self, request):
        query = request.data.get('query')
        print(query)


        i = Travels.objects.filter(travelsname__icontains=query) | Travels.objects.filter(travelslocation__icontains=query)
        for dta in i:
            print(dta)

        data = [{'travelsname': info.travelsname, 'travelsphone': info.travelsphone, 'travelslocation': info.travelslocation, 'travelspincode': info.travelspincode,'travelsrating': info.travelsrating, 'reviews': info.reviews}
                for info in i]
        return Response({'data': data, 'message': 'Successfully fetched', 'success': True}, status=status.HTTP_200_OK)


#Guide search
class GuideSearchAPIView(GenericAPIView):
    def post(self, request):
        query = request.data.get('query')
        print(query)


        i = Guide.objects.filter(guidename__icontains=query) | Guide.objects.filter(guidelocation__icontains=query)
        for dta in i:
            print(dta)

        data = [{'guidename': info.guidename, 'guidephone': info.guidephone, 'guidelocation': info.guidelocation, 'guidepincode': info.guidepincode,'guiderating': info.guiderating, 'Reviews': info.Reviews}
                for info in i]
        return Response({'data': data, 'message': 'Successfully fetched', 'success': True}, status=status.HTTP_200_OK)

#Add spot by user
class UseraddSpotsAPIView(GenericAPIView):
    serializer_class = SpotsSerializer

    def post(self, request):
        username=""
        Spotsname = request.data.get('Spotsname')
        Spotsclimat = request.data.get('Spotsclimat')
        Bestperiod = request.data.get('Bestperiod')
        description = request.data.get('description')
        Visiterscount = request.data.get('Visiterscount')
        Rating = request.data.get('Rating')
        Area = request.data.get('Area')
        Views=request.data.get('View')
        country = request.data.get('country')
        users = request.data.get('user')
        Spots_status="0"

        

        data = user.objects.filter(id=users).values()
        for i in data:
            username=i['name']
        
        
        serializer = self.serializer_class(data= {'Spotsname':Spotsname, 'Spotsclimat':Spotsclimat,'Bestperiod':Bestperiod,'description':description,'Visiterscount':Visiterscount,'Rating':Rating,'Area':Area,'View':Views,'country':country,'user':users,'username':username,'Spots_status':Spots_status})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'Spot added successfully', 'success':True}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)



# view all Spot 

class Get_All_SpotsAPIView(GenericAPIView):
    serializer_class = SpotsSerializer
    def get(self,request):
        queryset = Spots.objects.all()
        if(queryset.count()>0):
            serializer = SpotsSerializer(queryset,many= True)
   

            return Response({'data':serializer.data,'message':'all user data set','success' : True},status = status.HTTP_200_OK)
        else:
    
            return Response({'data':'non data available','success':False},status = status.HTTP_201_CREATED)


#single Spot view

class Get_single_SpotsAPIView(GenericAPIView):
    def get(self,request,id):
        queryset = Spots.objects.get(pk=id)
        serializer =SpotsSerializer(queryset)
        return Response({'data':serializer.data,'message':'single Spot data','success':True},status =status.HTTP_200_OK)




#Add Userprofile 
class addUserprofileAPIView(GenericAPIView):
    serializer_class = UserprofileSerializer

    def post(self, request):
        username=""
        Patrons = request.data.get('Patrons')
        Average = request.data.get('Average')
        Solo = request.data.get('Solo')
        Leadingcommunity = request.data.get('Leadingcommunity')
        Includingcommunity = request.data.get('Includingcommunity')
        Nextdestination = request.data.get('Nextdestination')
        users = request.data.get('user')
        Userprofile_status = '0'
           

        data = user.objects.filter(id=users).values()
        for i in data:
            username=i['name']
        
        
        serializer = self.serializer_class(data= {'Patrons':Patrons, 'Average':Average,'Solo':Solo,'Leadingcommunity':Leadingcommunity,'Includingcommunity':Includingcommunity,'Nextdestination':Nextdestination,'user':users,'username':username,'Userprofile_status':Userprofile_status})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'Spot added successfully', 'success':True}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)

#Userprofile Single view

class Get_single_UserprofileAPIView(GenericAPIView):
    def get(self,request,id):
        queryset = Userprofile.objects.get(pk=id)
        serializer =UserprofileSerializer(queryset)
        return Response({'data':serializer.data,'message':'single Userprofile data','success':True},status =status.HTTP_200_OK)


#Add Plannedtrip 


class PlannedtripAPIView(GenericAPIView):
    serializer_class = PlannedtripSerializer

    def post(self, request):
        username=""
        Startingpoint = request.data.get('Startingpoint')
        Destination = request.data.get('Destination')
        Days = request.data.get('Days')
        Nights = request.data.get('Nights')
        Plan = request.data.get('Plan')
        Guide = request.data.get('Guide')
        Travels = request.data.get('Travels')
        Persons = request.data.get('Persons')
        Budget = request.data.get('Budget')
        users = request.data.get('user')
        Plannedtrip_status = '0'
           

        data = user.objects.filter(id=users).values()
        for i in data:
            username=i['name']
        
        
        serializer = self.serializer_class(data= {'Startingpoint':Startingpoint, 'Destination':Destination,'Days':Days,'Nights':Nights,'Plan':Plan,'Guide':Guide,'Travels':Travels,'Persons':Persons,'Budget':Budget,'user':users,'username':username,'Plannedtrip_status':Plannedtrip_status})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'Plannedtrip added successfully', 'success':True}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)



# view all Plannedtrip

class Get_All_PlannedtripAPIView(GenericAPIView):
    serializer_class = PlannedtripSerializer
    def get(self,request):
        queryset = Plannedtrip.objects.all()
        if(queryset.count()>0):
            serializer = PlannedtripSerializer(queryset,many= True)
   

            return Response({'data':serializer.data,'message':'all Plannedtrip set','success' : True},status = status.HTTP_200_OK)
        else:
    
            return Response({'data':'non data available','success':False},status = status.HTTP_201_CREATED)


#single Plannedtrip view

class Get_single_PlannedtripAPIView(GenericAPIView):
    def get(self,request,id):
        queryset = Plannedtrip.objects.get(pk=id)
        serializer =PlannedtripSerializer(queryset)
        return Response({'data':serializer.data,'message':'single Plannedtrip data','success':True},status =status.HTTP_200_OK)

#Update Plannedtrip view
class Update_PlannedtripAPIView(GenericAPIView):
    serializer_class=PlannedtripSerializer
    def put(self,request,id):
        queryset = Plannedtrip.objects.get(pk=id)
        print(queryset)
        serializer = PlannedtripSerializer(instance = queryset,data=request.data,partial= True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'updated succesfully','success':True},status = status.HTTP_200_OK)
        else:
            return Response({'data':'something went wrong','success': False},status = status.HTTP_400_BAD_REQUEST)



#Add Comments 


class CommentsAPIView(GenericAPIView):
    serializer_class = CommentsSerializer

    def post(self, request):
        username=""
        spotname=""
        Commenttext = request.data.get('Commenttext')
        Createddate = request.data.get('Createddate')
        spots = request.data.get('spot')
        users = request.data.get('user')
        Commentsstatus = '0'
           

        data = user.objects.filter(id=users).values()
        for i in data:
            username=i['name']

        data2 = Spots.objects.filter(id=spots).values()
        for i in data2:
            spotname=i['Spotsname']
        
        
        serializer = self.serializer_class(data= {'Commenttext':Commenttext, 'Createddate':Createddate,'spot':spots,'user':users,'username':username,'spotname':spotname,'Commentsstatus':Commentsstatus})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'Plannedtrip added successfully', 'success':True}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)

# view all Comments

class Get_All_CommentsAPIView(GenericAPIView):
    serializer_class = CommentsSerializer
    def get(self,request):
        queryset = Comments.objects.all()
        if(queryset.count()>0):
            serializer = CommentsSerializer(queryset,many= True)
   

            return Response({'data':serializer.data,'message':'all Comments set','success' : True},status = status.HTTP_200_OK)
        else:
    
            return Response({'data':'non data available','success':False},status = status.HTTP_201_CREATED)

#single Comment view

class Get_single_CommentsAPIView(GenericAPIView):
    def get(self,request,id):
        queryset = Comments.objects.get(pk=id)
        serializer =CommentsSerializer(queryset)
        return Response({'data':serializer.data,'message':'single Comments data','success':True},status =status.HTTP_200_OK)


#Update Comment view
class Update_CommentsAPIView(GenericAPIView):
    serializer_class=CommentsSerializer
    def put(self,request,id):
        queryset = Comments.objects.get(pk=id)
        print(queryset)
        serializer = CommentsSerializer(instance = queryset,data=request.data,partial= True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'updated succesfully','success':True},status = status.HTTP_200_OK)
        else:
            return Response({'data':'something went wrong','success': False},status = status.HTTP_400_BAD_REQUEST)





#Add Notification 
class NotificationAPIView(GenericAPIView):
    serializer_class = NotificationSerializer

    def post(self, request):
        username=""
        Sender = request.data.get('Sender')
        Receiver = request.data.get('Receiver')
        Notification = request.data.get('Notification')
        Date = request.data.get('Date')
        Action = request.data.get('Action')
        users = request.data.get('user')
        Notificationstatus = '0'
           

        data = user.objects.filter(id=users).values()
        for i in data:
            username=i['name']

                 
        serializer = self.serializer_class(data= {'Sender':Sender, 'Receiver':Receiver,'Notification':Notification,'Date':Date,'Action':Action,'user':users,'Notificationstatus':Notificationstatus,'username':username})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'Notification added successfully', 'success':True}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)



# view all Notification

class Get_All_NotificationAPIView(GenericAPIView):
    serializer_class = NotificationSerializer
    def get(self,request):
        queryset = Notification.objects.all()
        if(queryset.count()>0):
            serializer = NotificationSerializer(queryset,many= True)
   

            return Response({'data':serializer.data,'message':'all Notification set','success' : True},status = status.HTTP_200_OK)
        else:
    
            return Response({'data':'non data available','success':False},status = status.HTTP_201_CREATED)

#single Notification view

class Get_single_NotificationAPIView(GenericAPIView):
    def get(self,request,id):
        queryset = Notification.objects.get(pk=id)
        serializer =NotificationSerializer(queryset)
        return Response({'data':serializer.data,'message':'single Notification data','success':True},status =status.HTTP_200_OK)


# #Update Notification
class Update_NotificationAPIView(GenericAPIView):
    serializer_class=NotificationSerializer
    def put(self,request,id):
        queryset = Notification.objects.get(pk=id)
        print(queryset)
        serializer = NotificationSerializer(instance = queryset,data=request.data,partial= True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'updated succesfully','success':True},status = status.HTTP_200_OK)
        else:
            return Response({'data':'something went wrong','success': False},status = status.HTTP_400_BAD_REQUEST)


#Add Hotel Packege 
class HotelAddPackegeAPIView(GenericAPIView):
    serializer_class = PackegeHotelSerializer

    def post(self, request):
        hotelname=""
        Packegename = request.data.get('Packegename')
        Destination = request.data.get('Destination')
        Price = request.data.get('Price')
        Startdate = request.data.get('Startdate')
        Enddate = request.data.get('Enddate')
        Bookingcount = request.data.get('Bookingcount')
        Packegestatus = '0'
        hotels =request.data.get('Hotel')
           

        data = Hotel.objects.filter(id=hotels).values()
        for i in data:
            hotelname=i['hotelname']

                 
        serializer = self.serializer_class(data= {'Packegename':Packegename, 'Destination':Destination,'Price':Price,'Startdate':Startdate,'Enddate':Enddate,'Bookingcount':Bookingcount,'Packegestatus':Packegestatus,'hotel':hotels,'hotelname':hotelname})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'Packege added successfully', 'success':True}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)

# view all PackegeHotel

class Get_All_PackegeHotelAPIView(GenericAPIView):
    serializer_class = PackegeHotelSerializer
    def get(self,request):
        queryset = PackegeHotel.objects.all()
        if(queryset.count()>0):
            serializer = PackegeHotelSerializer(queryset,many= True)
   

            return Response({'data':serializer.data,'message':'all PackegeHotel set','success' : True},status = status.HTTP_200_OK)
        else:
    
            return Response({'data':'non data available','success':False},status = status.HTTP_201_CREATED)

#single PackegeHotel view

class Get_single_PackegeHotelAPIView(GenericAPIView):
    def get(self,request,id):
        queryset = PackegeHotel.objects.get(pk=id)
        serializer =PackegeHotelSerializer(queryset)
        return Response({'data':serializer.data,'message':'single PackegeHotel data','success':True},status =status.HTTP_200_OK)

#Delete PackegeHotel
class Delete_PackegeHotelAPIView(GenericAPIView):
    def delete(self, request, id):
        delmember = PackegeHotel.objects.get(pk=id)
        delmember.delete()
        return Response({'message':'Deleted successfully', 'success':True}, status=status.HTTP_200_OK)


#Add Resort Packege 
class AddPackegeResortAPIView(GenericAPIView):
    serializer_class = PackegeResortSerializer

    def post(self, request):
        resortname=""
        Packegename = request.data.get('Packegename')
        Destination = request.data.get('Destination')
        Price = request.data.get('Price')
        Startdate = request.data.get('Startdate')
        Enddate = request.data.get('Enddate')
        Bookingcount = request.data.get('Bookingcount')
        Packegestatus = '0'
        Resorts =request.data.get('Resort')
           

        data = Resort.objects.filter(id=Resorts).values()
        for i in data:
            resortname=i['resortname']

                 
        serializer = self.serializer_class(data= {'Packegename':Packegename, 'Destination':Destination,'Price':Price,'Startdate':Startdate,'Enddate':Enddate,'Bookingcount':Bookingcount,'Packegestatus':Packegestatus,'Resort':Resorts,'resortname':resortname})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'Packege added successfully', 'success':True}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)

# view all PackegeResort

class Get_All_PackegeResortAPIView(GenericAPIView):
    serializer_class = PackegeResortSerializer
    def get(self,request):
        queryset = PackegeResort.objects.all()
        if(queryset.count()>0):
            serializer = PackegeResortSerializer(queryset,many= True)
   

            return Response({'data':serializer.data,'message':'all PackegeResort set','success' : True},status = status.HTTP_200_OK)
        else:
    
            return Response({'data':'non data available','success':False},status = status.HTTP_201_CREATED)

#single PackegeResort view

class Get_single_PackegeResortAPIView(GenericAPIView):
    def get(self,request,id):
        queryset = PackegeResort.objects.get(pk=id)
        serializer =PackegeResortSerializer(queryset)
        return Response({'data':serializer.data,'message':'single PackegeResort data','success':True},status =status.HTTP_200_OK)

#Delete PackegeResort

class Delete_PackegeResortAPIView(GenericAPIView):
    def delete(self, request, id):
        delmember = PackegeResort.objects.get(pk=id)
        delmember.delete()
        return Response({'message':'Deleted successfully', 'success':True}, status=status.HTTP_200_OK)

#Add Travel Packege 
class AddPackegeTravelsAPIView(GenericAPIView):
    serializer_class = PackegeTravelsSerializer

    def post(self, request):
        travelsname=""
        Packegename = request.data.get('Packegename')
        Destination = request.data.get('Destination')
        Price = request.data.get('Price')
        Startdate = request.data.get('Startdate')
        Enddate = request.data.get('Enddate')
        Bookingcount = request.data.get('Bookingcount')
        Packegestatus = '0'
        Travel =request.data.get('Travels')
      
           

        data = Travels.objects.filter(id=Travel).values()
        for i in data:
            travelsname=i['travelsname']

                 
        serializer = self.serializer_class(data= {'Packegename':Packegename, 'Destination':Destination,'Price':Price,'Startdate':Startdate,'Enddate':Enddate,'Bookingcount':Bookingcount,'Packegestatus':Packegestatus,'Travels':Travel,'travelsname':travelsname})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'Packege added successfully', 'success':True}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)

#Get all Travel packege
class Get_All_PackegeTravelsAPIView(GenericAPIView):
    serializer_class = PackegeTravelsSerializer
    def get(self,request):
        queryset = PackegeTravels.objects.all()
        if(queryset.count()>0):
            serializer = PackegeTravelsSerializer(queryset,many= True)
   

            return Response({'data':serializer.data,'message':'all PackegeTravels set','success' : True},status = status.HTTP_200_OK)
        else:
    
            return Response({'data':'non data available','success':False},status = status.HTTP_201_CREATED)

#single PackegeTravels view

class Get_single_PackegeTravelsAPIView(GenericAPIView):
    def get(self,request,id):
        queryset = PackegeTravels.objects.get(pk=id)
        serializer =PackegeTravelsSerializer(queryset)
        return Response({'data':serializer.data,'message':'single PackegeTravels data','success':True},status =status.HTTP_200_OK)


#Delete PackegeTravels

class Delete_PackegeTravelsAPIView(GenericAPIView):
    def delete(self, request, id):
        delmember = PackegeTravels.objects.get(pk=id)
        delmember.delete()
        return Response({'message':'Deleted successfully', 'success':True}, status=status.HTTP_200_OK)

#Add Chatcommunity
class ChatcommunityAPIView(GenericAPIView):
    serializer_class = ChatcommunitySerializer

    def post(self, request):
        username=""
        Communityname = request.data.get('Communityname')
        Chat = request.data.get('Chat')
        Createdtime = request.data.get('Createdtime')
        Uploaddate = request.data.get('Uploaddate')
        users = request.data.get('user')
        Chatcommunitystatus = '0'
           
        data = user.objects.filter(id=users).values()
        for i in data:
            username=i['name']

                 
        serializer = self.serializer_class(data= {'Communityname':Communityname, 'Chat':Chat,'Createdtime':Createdtime,'Uploaddate':Uploaddate,'user':users,'Chatcommunitystatus':Chatcommunitystatus,'username':username})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'Notification added successfully', 'success':True}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)


#Get all Chat
class Get_All_ChatcommunityAPIView(GenericAPIView):
    serializer_class = ChatcommunitySerializer
    def get(self,request):
        queryset =  Chatcommunity.objects.all()
        if(queryset.count()>0):
            serializer = ChatcommunitySerializer(queryset,many= True)
   

            return Response({'data':serializer.data,'message':'all Chatcommunity_chat set','success' : True},status = status.HTTP_200_OK)
        else:
    
            return Response({'data':'non data available','success':False},status = status.HTTP_201_CREATED)

#single Chat view

class Get_single_chat(GenericAPIView):
    def get(self,request,id):
        queryset = Chatcommunity.objects.get(pk=id)
        serializer =ChatcommunitySerializer(queryset)
        return Response({'data':serializer.data,'message':'single Chat data','success':True},status =status.HTTP_200_OK)

#Delete Chat

class Delete_chatAPIView(GenericAPIView):
    def delete(self, request, id):
        delmember = Chatcommunity.objects.get(pk=id)
        delmember.delete()
        return Response({'message':'Deleted successfully', 'success':True}, status=status.HTTP_200_OK)





#Add Reels
class AddReelsAPIView(GenericAPIView):
    serializer_class = ReelsSerializer

    def post(self, request):
        username=""
        Reelslength = request.data.get('Reelslength')
        Reels = request.data.get('Reels')
        Description = request.data.get('Description')
        Spotname = request.data.get('Spotname')
        Uploaddate = request.data.get('Uploaddate')
        users = request.data.get('user')
        Reelsstatus = '0'
           
        data = user.objects.filter(id=users).values()
        for i in data:
            username=i['name']

                 
        serializer = self.serializer_class(data= {'Reelslength':Reelslength, 'Reels':Reels,'Description':Description,'Spotname':Spotname,'Uploaddate':Uploaddate,'user':users,'Reelsstatus':Reelsstatus,'username':username})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'Reels added successfully', 'success':True}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)


#Get all Reels
class Get_All_ReelsAPIView(GenericAPIView):
    serializer_class = ReelsSerializer
    def get(self,request):
        queryset =  Reels.objects.all()
        if(queryset.count()>0):
            serializer = ReelsSerializer(queryset,many= True)
   

            return Response({'data':serializer.data,'message':'all Reels set','success' : True},status = status.HTTP_200_OK)
        else:
    
            return Response({'data':'non data available','success':False},status = status.HTTP_201_CREATED)

#single reel view

class Get_single_Reel(GenericAPIView):
    def get(self,request,id):
        queryset = Reels.objects.get(pk=id)
        serializer =ReelsSerializer(queryset)
        return Response({'data':serializer.data,'message':'single Reel data','success':True},status =status.HTTP_200_OK)


#Delete Reel

class Delete_Reel(GenericAPIView):
    def delete(self, request, id):
        delmember = Reels.objects.get(pk=id)
        delmember.delete()
        return Response({'message':'Deleted successfully', 'success':True}, status=status.HTTP_200_OK)

#resort booking
class ResortbookingApi(GenericAPIView):
    serializer_class = ResortbookingSerializer

    def post(self, request):
        username=""
        resortname=""
        noofpersons = request.data.get('noofpersons')
        phone = request.data.get('phone')
        checkindate = request.data.get('checkindate')
        checkintime = request.data.get('checkintime')
        checkoutdate = request.data.get('checkoutdate')
        resorts = request.data.get('resort')
        users = request.data.get('user')
        bookingstatus = '0'
           

        data = user.objects.filter(id=users).values()
        for i in data:
            username=i['name']

        data2 = Resort.objects.filter(id=resorts).values()
        for i in data2:
            resortname=i['resortname']
        
        
        serializer = self.serializer_class(data= {'noofpersons':noofpersons,'phone':phone,'checkindate':checkindate,'checkintime':checkintime,'checkoutdate':checkoutdate,'resort':resorts,'user':users,'username':username,'resortname':resortname,'bookingstatus':bookingstatus})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'ResortBocking added successfully', 'success':True}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)


class Get_All_ResortbookingAPIView(GenericAPIView):
    serializer_class = ResortbookingSerializer

    def get(self, request):
        queryset = Resortbooking.objects.all()
        
        if queryset.exists():
            serializer = self.serializer_class(queryset, many=True)
            return Response({'data': serializer.data, 'message': 'All Resort bookings', 'success': True}, status=status.HTTP_200_OK)
        else:
            return Response({'data': 'No data available', 'success': False}, status=status.HTTP_200_OK)



#single Resortbooking view

class Get_single_Resortbooking(GenericAPIView):
    def get(self,request,id):
        queryset = Resortbooking.objects.get(pk=id)
        serializer =ResortbookingSerializer(queryset)
        return Response({'data':serializer.data,'message':'single Resort booking data','success':True},status =status.HTTP_200_OK)

#delete Resort booking
class Delete_Resortbooking(GenericAPIView):
    def delete(self, request, id):
        delmember = Resortbooking.objects.get(pk=id)
        delmember.delete()
        return Response({'message':'Deleted successfully', 'success':True}, status=status.HTTP_200_OK)


#Hotel booking
class HotelbookingApi(GenericAPIView):
    serializer_class = HotelbookingSerializer

    def post(self, request):
        username=""
        hotelname=""
        noofpersons = request.data.get('noofpersons')
        phone = request.data.get('phone')
        checkindate = request.data.get('checkindate')
        checkintime = request.data.get('checkintime')
        checkoutdate = request.data.get('checkoutdate')
        hotels = request.data.get('hotel')
        users = request.data.get('user')
        bookingstatus = '0'
           

        data = user.objects.filter(id=users).values()
        for i in data:
            username=i['name']

        data2 = Hotel.objects.filter(id=hotels).values()
        for i in data2:
            hotelname=i['hotelname']
        
        
        serializer = self.serializer_class(data= {'noofpersons':noofpersons,'phone':phone,'checkindate':checkindate,'checkintime':checkintime,'checkoutdate':checkoutdate,'hotel':hotels,'user':users,'username':username,'hotelname':hotelname,'bookingstatus':bookingstatus})
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'HotelBocking added successfully', 'success':True}, status = status.HTTP_201_CREATED)
        return Response({'data':serializer.errors, 'message':'Failed','success':False}, status=status.HTTP_400_BAD_REQUEST)

#get all hotel booking
class Get_All_HotelbookingAPIView(GenericAPIView):
    serializer_class = HotelbookingSerializer

    def get(self, request):
        queryset = Hotelbooking.objects.all()
        
        if queryset.exists():
            serializer = self.serializer_class(queryset, many=True)
            return Response({'data': serializer.data, 'message': 'All Hotel bookings', 'success': True}, status=status.HTTP_200_OK)
        else:
            return Response({'data': 'No data available', 'success': False}, status=status.HTTP_200_OK)


#single Hotelbooking view

class Get_single_Hotelbooking(GenericAPIView):
    def get(self,request,id):
        queryset = Hotelbooking.objects.get(pk=id)
        serializer =HotelbookingSerializer(queryset)
        return Response({'data':serializer.data,'message':'single Resort booking data','success':True},status =status.HTTP_200_OK)

#delete Hotel booking
class Delete_Hotelbooking(GenericAPIView):
    def delete(self, request, id):
        delmember = Hotelbooking.objects.get(pk=id)
        delmember.delete()
        return Response({'message':'Deleted successfully', 'success':True}, status=status.HTTP_200_OK)
