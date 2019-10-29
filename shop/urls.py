from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('evening_walk/', views.evening_walk, name='evening_walk'), 
    path('zymjoin/', views.zymjoin, name='zymjoin'), 
    path('junkfood/', views.junkfood, name='junkfood'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),


    ]