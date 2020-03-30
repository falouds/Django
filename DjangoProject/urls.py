"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .view import db,login,dataOperation
from django.conf.urls import url
urlpatterns = [ 
    url('upload/',db.saveData,name='upload'),
    url('downloadData/',db.downloadData,name='download'),
    url('loginPage/',login.loginPage,name='login'),
    url('signupPage/',login.signupPage,name='signup'),
    url('index/',login.successLogin,name='index'),
    url('diagram/',dataOperation.diagram,name='diagram'), 

    url('login/',login.login),
    url('signup/',login.signup),
    url('save/',db.saveDB,name='save'),
    url('download/',db.downloadDB),
]
