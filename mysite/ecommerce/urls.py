from django.urls import path
from django.contrib.auth.decorators import login_required 
from . import views

app_name="ecommerce"


urlpatterns = [
    path('', login_required(views.home), name = 'home'),
    path('my_tickets/', login_required(views.order_list), name='order_list'),
    path('logout/', views.logout, name = 'logout'),
    
]
