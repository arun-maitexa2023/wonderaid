from django.shortcuts import render,redirect
from .serializers import loginUsersSerializer,UserRegisterSerializer,HotelRegisterSerializer,RestaurentRegisterSerializer,ResortRegisterSerializer,TravelsRegisterSerializer,GuideRegisterSerializer
from .models import log, user, Hotel, Restaurent, Resort, Travels, Guide
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
