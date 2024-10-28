from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('changepassword',views.changepassword,name='changepassword'),
    path('setpassword',views.setpassword,name='setpassword'),
    path('newpassword',views.newpassword,name='newpassword'),
    path('cart/<int:id>',views.cart,name='cart'),
    path('details/<str:name>',views.details,name='details'),
    path('confirm',views.confirm,name='confirm'),
    path('thanks',views.thanks,name='thanks'),

    
]