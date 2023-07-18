from django.urls import path
from wanderaid import views

urlpatterns =[

    path('',views.index,name='index'),
   
    
    
    

   
    path('Requested_Travels',views.Requested_Travels,name='Requested_Travels'),
    
    path('view_users',views.view_users,name='view_users'),
#Hotel
    path('Approved_Hotels',views.Approved_Hotels,name='Approved_Hotels'),
    path('Requested_Hotels',views.Requested_Hotels,name='Requested_Hotels'),
    path('admin_approve_hotel/<int:id>',views.admin_approve_hotel,name='admin_approve_hotel'),
    path('admin_reject_hotel/<int:id>',views.admin_reject_hotel,name='admin_reject_hotel'),
#Restaurents
    path('Approved_Restaurents',views.Approved_Restaurents,name='Approved_Restaurents'),
    path('Requested_Restaurents',views.Requested_Restaurents,name='Requested_Restaurents'),
    path('admin_approve_Restaurents/<int:id>',views.admin_approve_Restaurents,name='admin_approve_Restaurents'),
    path('admin_reject_Restaurents/<int:id>',views.admin_reject_Restaurents,name='admin_reject_Restaurents'),
#Resort

    path('Requested_Resorts',views.Requested_Resorts,name='Requested_Resorts'),
    path('Approved_Resorts',views.Approved_Resorts,name='Approved_Resorts'),
    path('admin_approve_Resorts/<int:id>',views.admin_approve_Resorts,name='admin_approve_Resorts'),
    path('admin_reject_Resorts/<int:id>',views.admin_reject_Resorts,name='admin_reject_Resorts'),


# travels

    path('Approved_Travels',views.Approved_Travels,name='Approved_Travels'),
    path('Requested_Travels',views.Requested_Travels,name='Requested_Travels'),
    path('admin_approve_Travels/<int:id>',views.admin_approve_Travels,name='admin_approve_Travels'),
    path('admin_reject_Travels/<int:id>',views.admin_reject_Travels,name='admin_reject_Travels'),

#Guides

    # travels

    path('Approved_Guide',views.Approved_Guide,name='Approved_Guide'),
    path('Requested_Guide',views.Requested_Guide,name='Requested_Guide'),
    path('admin_approve_Guide/<int:id>',views.admin_approve_Guide,name='admin_approve_Guide'),
    path('admin_reject_Guide/<int:id>',views.admin_reject_Guide,name='admin_reject_Guide'),

]

