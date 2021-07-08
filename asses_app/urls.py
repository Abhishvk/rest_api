
from django.contrib import admin
from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.home),
    path('cuser',v.CreateUser.as_view()),
    path('cclient',v.CreateClient.as_view()),
    path('lclient',v.ListClient.as_view()),
    path('rudclient/<int:pk>',v.RUDClient.as_view()),

    path('cproject',v.CreateProject.as_view()),
    path('rproject/<int:pk>',v.RProject.as_view())
    
]
