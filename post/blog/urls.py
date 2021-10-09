from django.urls import path
from .views import dashboard, delete, editt, home , about ,contact, singup, user_login, user_logout
urlpatterns = [
    path('', home,name='home'),
    path('about', about,name='about'),
    path('contact', contact,name='contact'),
    path('dashboard', dashboard,name='dashboard'),
    path('logout', user_logout,name='logout'),
    path('login', user_login,name='login'),
    path('singup', singup,name='singup'),
    path('delete/<int:id>/', delete, name="delete"),
    path('edit/<int:id>/',editt,name="edit"),


]
