# -*- coding: utf-8 -*-
 
from TestModel.models import User
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render_to_response,render
from django.views.decorators import csrf
from django.core import serializers
import math,json,time
# # 表单
def loginPage(request):
    return render_to_response('login/login.html')
def signupPage(request):
    return render_to_response('login/register.html')
def successLogin(request):
    return render(request,'index.html',{'log':True})

def signup(request):
    request.encoding='utf-8'
    context = {}
    response = {}
    if(request.method == 'POST'):    
        response['user'] = request.POST.get('name', '')
        response['password'] = request.POST.get('password', '')
        userqs = User.objects.filter(user=response['user'])
        if(not userqs.exists()):
            users = User(
                id = math.ceil(time.time()),
                user = response['user'],
                password = response['password'],
            )
            users.save()
            context['text'] = '注册成功'
            context['code'] = 1
        else:
            context['text'] = '用户已存在'
            context['code'] = -1
    else:
        context['text'] = '请求错误'
        context['code'] = -3
    return JsonResponse(context)

def login(request):
    request.encoding='utf-8'
    context = {}
    response = {}
    if(request.method == 'POST'):
        response['user'] = request.POST.get('user', '')
        response['password'] = request.POST.get('password', '')
        userqs = User.objects.filter(user=response['user'])
        print("respomse" + str(response))
        if(userqs.exists() and userqs.count()==1):
            if(userqs[0].password==response['password']):
                context['text'] = '登陆成功'
                context['code'] = 1
            else:
                context['text'] = '用户名或密码错误'
                context['code'] = -1
        else:
                context['text'] = '用户名错误'
                context['code'] = -2
    else:
        context['text'] = '请求错误'
        context['code'] = -3       
    return JsonResponse(context)
        