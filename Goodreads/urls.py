"""Goodreads URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from Views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path("loginpage",loginpage),
    path("login",login),
    path("addadmin",addadmin),
    path("showadmin",showadmin),
    path("editadmin",editadmin),
    path("saveadmin",save),
    path("changepassword",changepassword),
    path("updatepassword",updatepassword),
    path("removeadmin",removeadmin),
    path("addcategory",addcategory),
    path("insertcategory",insertcategory),
    path("showcategory", showcategory),
    path("removecategory",removecategory),
    path("editcategory",editcategory),
    path("savecategory",save),
    path("addbook",addbook),
    path("insertbook",insertbook),
    # path("showbook",showbook),
    # path("getbooks",getbooks),
    # path("deleteaction",deleteaction),
    # path("editdataaction",editdataaction),
    # path("showbook2",showbook)
    path("booksview",booksview),
    path("viewbooks",viewbooks),
    path("deltebooks",deltebooks),
    path("editbook",editbook),
]
