from django.urls import path
from . import views

urlpatterns =[

   path('register_users',views.userRegisterAPIView.as_view(), name='register_users'),

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
]