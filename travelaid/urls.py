from django.urls import path
from . import views

urlpatterns =[

   path('userRegisterAPIView',views.userRegisterAPIView.as_view(), name='userRegisterAPIView'),

   path('register_hotels',views.HotelRegisterAPIView.as_view(), name='register_hotels'),

   path('register_restaurents',views.RestaurentRegisterAPIView.as_view(), name='register_restaurents'),

   path('register_resorts',views.ResortRegisterAPIView.as_view(), name='register_resorts'),

   path('register_travels',views.TravelsRegisterAPIView.as_view(), name='register_travels'),

   path('register_guides',views.GuideRegisterAPIView.as_view(), name='register_guides'),

   path('login',views.LoginAPIView.as_view(), name='login'),

   path('view_get_all_users',views.Get_All_UsersAPIView.as_view(), name='view_get_all_users'),

   path('view_single_users/<int:id>',views.Get_single_UserAPIView.as_view(), name='view_single_users'),

   path('update_user/<int:id>',views.Update_UserAPIView.as_view(), name='update_user'),

   path('view_get_all_hotels',views.Get_All_HotelsAPIView.as_view(), name='view_get_all_hotels'),

   path('view_single_hotel/<int:id>',views.Get_single_HotelAPIView.as_view(), name='view_single_hotel'),

   path('update_hotel/<int:id>',views.Update_HotelAPIView.as_view(), name='update_hotel'),

   path('view_get_all_restaurents',views.Get_All_RestaurentsAPIView.as_view(), name='view_get_all_restaurents'),

   path('view_single_restaurent/<int:id>',views.Get_single_RestaurentAPIView.as_view(), name='view_single_restaurent'),

   path('update_restaurent/<int:id>',views.Update_RestaurentAPIView.as_view(), name='update_restaurent'),

   path('view_get_all_resorts',views.Get_All_ResortsAPIView.as_view(), name='view_get_all_resorts'),

   path('view_single_resort/<int:id>',views.Get_single_ResortAPIView.as_view(), name='view_single_resort'),

   path('update_resort/<int:id>',views.Update_ResortAPIView.as_view(), name='update_resort'),

   path('view_get_all_travels',views.Get_All_TravelsAPIView.as_view(), name='view_get_all_travels'),

   path('view_single_travels/<int:id>',views.Get_single_TravelsAPIView.as_view(), name='view_single_travels'),

   path('update_travels/<int:id>',views.Update_TravelsAPIView.as_view(), name='update_travels'),



   path('view_get_all_guides',views.Get_All_GuidesAPIView.as_view(), name='view_get_all_guides'),

   path('view_single_guide/<int:id>',views.Get_single_GuideAPIView.as_view(), name='view_single_guide'),

   path('update_guide/<int:id>',views.Update_GuideAPIView.as_view(), name='update_guide'),


   #add more details user

   path('Moredetails_of_User_APIView/<int:id>',views.Moredetails_of_User_APIView.as_view(), name='Moredetails_of_User_APIView'),

   #add more details Hotel

   path('Moredetails_of_Hotel_APIView/<int:id>',views.Moredetails_of_Hotel_APIView.as_view(), name='Moredetails_of_Hotel_APIView'),
   #add more details Restaurent

   path('Moredetails_of_Restaurent_APIView/<int:id>',views.Moredetails_of_Restaurent_APIView.as_view(), name='Moredetails_of_Restaurent_APIView'),


   #add more details Resort

   path('Moredetails_of_Resort_APIView/<int:id>',views.Moredetails_of_Resort_APIView.as_view(), name='Moredetails_of_Resort_APIView'),

   #add more details Travels

   path('Moredetails_of_Travels_APIView/<int:id>',views.Moredetails_of_Travels_APIView.as_view(), name='Moredetails_of_Travels_APIView'),

   #add more details Guide

   path('Moredetails_of_Guide_APIView/<int:id>',views.Moredetails_of_Guide_APIView.as_view(), name='Moredetails_of_Guide_APIView'),

   #filter Hotel by location or name
   path('HotelsSearchAPIView',views.HotelsSearchAPIView.as_view(), name='HotelsSearchAPIView'),
   
   
   #filter Restaurent by location or name
   path('RestaurentSearchAPIView',views.RestaurentSearchAPIView.as_view(), name='RestaurentSearchAPIView'),
  
  #filter Resort by location or name
   path('ResortSearchAPIView',views.ResortSearchAPIView.as_view(), name='ResortSearchAPIView'),
  
   #filter Travels by location or name
   path('ResortSearchAPIView',views.ResortSearchAPIView.as_view(), name='ResortSearchAPIView'),

   #filter Guide by location or name
   path('GuideSearchAPIView',views.GuideSearchAPIView.as_view(), name='GuideSearchAPIView'),

   #filter Travels by location or name
   path('TravelsSearchAPIView',views.TravelsSearchAPIView.as_view(), name='TravelsSearchAPIView'),
   #Add spot
   path('UseraddSpotsAPIView',views.UseraddSpotsAPIView.as_view(), name='UseraddSpotsAPIView'),

   #view all spot
   path('Get_All_SpotsAPIView',views.Get_All_SpotsAPIView.as_view(), name='Get_All_SpotsAPIView'),

   #view Single spot
   path('Get_single_SpotsAPIView/<int:id>',views.Get_single_SpotsAPIView.as_view(), name='Get_single_SpotsAPIView'),

   #view addUserprofile
   path('addUserprofileAPIView',views.addUserprofileAPIView.as_view(), name='addUserprofileAPIView'),

   #view Single addUserprofile
   path('Get_single_UserprofileAPIView/<int:id>',views.Get_single_UserprofileAPIView.as_view(), name='Get_single_UserprofileAPIView'),

   #Add plande trip
   path('PlannedtripAPIView',views.PlannedtripAPIView.as_view(), name='PlannedtripAPIView'),

   #view all plande trip
   path('Get_All_PlannedtripAPIView',views.Get_All_PlannedtripAPIView.as_view(), name='Get_All_PlannedtripAPIView'),

   #view Single plande trip
   path('Get_single_PlannedtripAPIView/<int:id>',views.Get_single_PlannedtripAPIView.as_view(), name='Get_single_PlannedtripAPIView'),

   #update plande trip
   path('Update_PlannedtripAPIView/<int:id>',views.Update_PlannedtripAPIView.as_view(), name='Update_PlannedtripAPIView'),


   #Comments
   path('CommentsAPIView',views.CommentsAPIView.as_view(), name='CommentsAPIView'),

   #view all Comments
   path('Get_All_CommentsAPIView',views.Get_All_CommentsAPIView.as_view(), name='Get_All_CommentsAPIView'),


   #view Single Comments trip
   path('Get_single_CommentsAPIView/<int:id>',views.Get_single_CommentsAPIView.as_view(), name='Get_single_CommentsAPIView'),
 
 
   #update Comments
   path('Update_CommentsAPIView/<int:id>',views.Update_CommentsAPIView.as_view(), name='Update_CommentsAPIView'),

   #Add Notification
   path('NotificationAPIView',views.NotificationAPIView.as_view(), name='NotificationAPIView'),


  #view all Comments
   path('Get_All_NotificationAPIView',views.Get_All_NotificationAPIView.as_view(), name='Get_All_NotificationAPIView'),

    #view Single Comments trip
   path('Get_single_NotificationAPIView/<int:id>',views.Get_single_NotificationAPIView.as_view(), name='Get_single_NotificationAPIView'),
 
   #update Comments
   path('Update_NotificationAPIView/<int:id>',views.Update_NotificationAPIView.as_view(), name='Update_NotificationAPIView'),


   #Add Hitel Packege
   path('HotelAddPackegeAPIView',views.HotelAddPackegeAPIView.as_view(), name='HotelAddPackegeAPIView'),

   #View all HotelPackege
   path('Get_All_PackegeHotelAPIView',views.Get_All_PackegeHotelAPIView.as_view(), name='Get_All_PackegeHotelAPIView'),

   #view Single HotelPackege
   path('Get_single_PackegeHotelAPIView/<int:id>',views.Get_single_PackegeHotelAPIView.as_view(), name='Get_single_PackegeHotelAPIView'),
  
   #Delete HotelPackege
   path('Delete_PackegeHotelAPIView/<int:id>',views.Delete_PackegeHotelAPIView.as_view(), name='Delete_PackegeHotelAPIView'),
 
   #Add Resort Packege
   path('AddPackegeResortAPIView',views.AddPackegeResortAPIView.as_view(), name='AddPackegeResortAPIView'),

 
 
   #View all HotelPackege
   path('Get_All_PackegeResortAPIView',views.Get_All_PackegeResortAPIView.as_view(), name='Get_All_PackegeResortAPIView'),

 
   #view Single PackegeResort
   path('Get_single_PackegeResortAPIView/<int:id>',views.Get_single_PackegeResortAPIView.as_view(), name='Get_single_PackegeResortAPIView'),
  
   #Delete PackegeResort
   path('Delete_PackegeResortAPIView/<int:id>',views.Delete_PackegeResortAPIView.as_view(), name='Delete_PackegeResortAPIView'),
 
   #Add Travels Packege
   path('AddPackegeTravelsAPIView',views.AddPackegeTravelsAPIView.as_view(), name='AddPackegeTravelsAPIView'),

   #View all TravelPackege
   path('Get_All_PackegeTravelsAPIView',views.Get_All_PackegeTravelsAPIView.as_view(), name='Get_All_PackegeTravelsAPIView'),


   #view Single PackegeTravels
   path('Get_single_PackegeTravelsAPIView/<int:id>',views.Get_single_PackegeTravelsAPIView.as_view(), name='Get_single_PackegeTravelsAPIView'),
  
   #Delete PackegeTravels
   path('Delete_PackegeTravelsAPIView/<int:id>',views.Delete_PackegeTravelsAPIView.as_view(), name='Delete_PackegeTravelsAPIView'),
 
   #Add Chat
   path('ChatcommunityAPIView',views.ChatcommunityAPIView.as_view(), name='ChatcommunityAPIView'),

   #View all Chat
   path('Get_All_ChatcommunityAPIView',views.Get_All_ChatcommunityAPIView.as_view(), name='Get_All_ChatcommunityAPIView'),


   #view Single chat
   path('Get_single_chat/<int:id>',views.Get_single_chat.as_view(), name='Get_single_chat'),
  
   #Delete chat
   path('Delete_chatAPIView/<int:id>',views.Delete_chatAPIView.as_view(), name='Delete_chatAPIView'),

   #Add Reels
   path('AddReelsAPIView',views.AddReelsAPIView.as_view(), name='AddReelsAPIView'),

   #View all Reels
   path('Get_All_ReelsAPIView',views.Get_All_ReelsAPIView.as_view(), name='Get_All_ReelsAPIView'),
   #view Single Reel
   path('Get_single_Reel/<int:id>',views.Get_single_Reel.as_view(), name='Get_single_Reel'),
  
   #Delete Reel
   path('Delete_Reel/<int:id>',views.Delete_Reel.as_view(), name='Delete_Reel'),

   #Resortbooking
   path('ResortbookingApi',views.ResortbookingApi.as_view(), name='ResortbookingApi'),
   
   #view all resort booking
   path('Get_All_ResortbookingAPIView',views.Get_All_ResortbookingAPIView.as_view(), name='Get_All_ResortbookingAPIView'),
  
   #view Single Resort booking
   path('Get_single_Resortbooking/<int:id>',views.Get_single_Resortbooking.as_view(), name='Get_single_Resortbooking'),
   
   #Delete Resort booking
   path('Delete_Resortbooking/<int:id>',views.Delete_Resortbooking.as_view(), name='Delete_Resortbooking'),

   #Hotelbooking
   path('HotelbookingApi',views.HotelbookingApi.as_view(), name='HotelbookingApi'),
   
   #view all Hotel booking
   path('Get_All_HotelbookingAPIView',views.Get_All_HotelbookingAPIView.as_view(), name='Get_All_HotelbookingAPIView'),
  
   #view Single Hotel booking
   path('Get_single_Hotelbooking/<int:id>',views.Get_single_Hotelbooking.as_view(), name='Get_single_Hotelbooking'),
   
  #Delete Resort booking
   path('Delete_Hotelbooking/<int:id>',views.Delete_Hotelbooking.as_view(), name='Delete_Hotelbooking'),




   #Delete User
   path('Delete_userAPIView/<int:log_id>',views.Delete_userAPIView.as_view(), name='Delete_userAPIView'),

   
]