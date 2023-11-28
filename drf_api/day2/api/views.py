from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("成功")

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.request import Request
class UserView(APIView):
    def get(self,request):
        print(request.user) #当前登录用户 -> 匿名用户
        print(request.auth)
        return Response("测试成功")