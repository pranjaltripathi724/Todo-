from django.urls import path
from . import views
from django.contrib import admin 


urlpatterns = [
    path('one/',views.one),
    path('addtask/',views.addtask),
    path('delete/<int:id>',views.delete),
    path('edit/<int:id>',views.edit),
    path('show/',views.show),
    path('signup/',views.user_signup),
    path('login/',views.user_login),
    path('logout/',views.user_logout),

]