
from django.urls import path,include
from Home import views

urlpatterns = [
    path('',views.Home,name='Home'),
    path('login',views.Login,name='Login'),
    path('logout',views.Logout,name='Logout'),
    path('register',views.Register,name='Register'),
    
]