# -*- coding: utf-8 -*-
# @Time    : 2020-08-02 22:25
# @Author  : liudongyang
# @FileName: views.py
# @Software: PyCharm
from django.shortcuts import render,get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.decorators import login_required
from sign.models import Event, Guest
# 分页
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


import time
import datetime
def index(request):
    return render(request, 'index.html')


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username,make_password(password))
    user = auth.authenticate(username=username, password=password)  # active为false是，会验证不通过
    # if password == '1234' and username == 'zhangsan':
    print(user)
    if user is not None:
        auth.login(request,user)  # 登录
        # response.set_cookie('user', username, 3600)
        request.session['user'] = username
        response =  HttpResponseRedirect('event_manage/')
        return response
    else:
        return render(request, 'index.html',{'code': 400, 'error': 'username or password error!'})

@login_required
def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/index/')
    return response

@login_required
def event_manage(request):
    # username = request.COOKIES.get('user')
    event_list = Event.objects.all()
    username = request.session.get('user', '')
    for even in event_list:
        # print(even.start_time,type(even.start_time))
        even.start_time = str(even.start_time)[:19]  # 格式转换
        # 转码
        if even.status:
            even.status = '未开始'
        else:
            even.status = '已结束'

    return render(request, 'event_manage.html',{"username": username, 'eventlist': event_list})

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

@login_required
def search_name(request):
    username = request.session.get('user', '')
    name = request.GET.get('name', '')
    # print(name)
    result = Event.objects.filter(name__contains=name)
    # print(result)
    # for i in result:
    #     print(i)
    return render(request, 'event_manage.html', {'user':username,'eventlist': result})

# 嘉宾管理
@login_required
def guest_manage(request):
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()
    page_num = 2
    page = request.GET.get('page')
    single_page = Paginator(guest_list, page_num)
    try:
        contacts = single_page.page(page)
    except PageNotAnInteger:
        contacts = single_page.page(1)
    except EmptyPage:
        contacts = single_page.page(single_page.num_pages)

    for con in contacts:
        print(con,type(con))
        if con.sign:
            con.sign = '已签到'
        else:
            con.sign = '未签到'
    return render(request, "guest_manage.html", {"user": username,
                                                          "guests": contacts})

# 签到
@login_required
def sign_index(request,eid):
    username = request.session.get('user', '')
    event = get_object_or_404(Event, id=eid)
    signed = Guest.objects.filter(event=eid).filter(sign=True).count()
    print('signed',signed)
    print('sign_index', eid)
    return render(request, 'sign_index.html', {'event': event, 'signed':signed,'user':username})


@login_required
def sign_index_action(request, eid):
    event = get_object_or_404(Event, id=eid)
    phone = request.POST.get('phone', '')
    username = request.session.get('user', '')

    print(phone)
    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request, 'sign_index.html', {'event': event,'hint': 'phone error.','user':username})
    result = Guest.objects.filter(phone=phone, event_id=eid)
    if not result:
        return render(request, 'sign_index.html', {'event': event, 'hint': 'event id or phone error.','user':username})
    result = Guest.objects.get(phone=phone, event_id=eid)
    if result.sign:
        return render(request, 'sign_index.html', {'event': event, 'hint': "user has sign in.",'user':username})
    else:
        Guest.objects.filter(phone=phone, event_id=eid).update(sign='1')
        return render(request, 'sign_index.html', {'event': event,'hint': 'sign in success!','guest': result,'user':username})