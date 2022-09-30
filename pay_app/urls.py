from django.urls import path
from pay_app import views

app_name = 'pay_app'


urlpatterns = [ 
 
    path('initiate_pay/', views.initiate_payment, name='initiate-payment'), 
    path('<str:ref>/', views.verify_payment, name='verify-payment'),  
       
    
]
