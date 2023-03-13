from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.expception_handler import MyCustomError

from rest_framework import generics, status

from . import serializer
from .serializer import AdminSerializer
from .models import Admin


# Create your views here.
def main(request):
    return HttpResponse("<h3>Hellow</h3>")


# class Adminview(generics.CreateAPIView):
#     queryset = Admin.objects.all()
#     serializer_class = adminseralizer

class AdminView(APIView):
    admin_serializer = AdminSerializer

    def post(self, request):
        data = request.data
        serializer = self.admin_serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:

            try:
                # some code that may raise MyCustomError
                raise MyCustomError("This is a custom error message", "4002")
            except MyCustomError as e:
                return print(e.message, e.error_code)
                return Response(status=status.HTTP_400_BAD_REQUEST,)