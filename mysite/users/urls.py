from django.urls import path

from . import views
app_name="users"

urlpatterns = [
    path('registration/', views.registration),
    path('login/', views.login),
    
]
