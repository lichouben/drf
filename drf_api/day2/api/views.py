from django.shortcuts import render,HttpResponse

# Create your views here.
# def home(request):
    # return HttpResponse("成功")

from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from ext.auth import myAuthentication
class loginView(APIView):
    authentication_classes = []
    def get(self,request):
        print(request.user,request.auth) #当前登录用户 -> 匿名用户
        return Response("LoginView")
    
class UserView(APIView):
    authentication_classes=[myAuthentication,]

    def get(self,request):
        print(request.user,request.auth) #当前登录用户 -> 匿名用户

        return Response("UserView")

    
class orderView(APIView):
    # authentication_classes=[myAuthentication,]
    def get(self,request):
        print(request.user,request.auth) #当前登录用户 -> 匿名用户
        return Response("orderView")