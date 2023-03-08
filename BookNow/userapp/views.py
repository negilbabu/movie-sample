import datetime
from django.http import HttpResponse
from django.urls import include,path
from django.shortcuts import render
from userapp import views
# Create your views here.
def current_datetime(request):
    now=datetime.datetime.now()
    html="<html><body>It is now %s. </body></html>" % now
    return HttpResponse(html)