from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username,password)
    if password == '1234' and username == 'zhangsan':
        return HttpResponseRedirect('event_manage/')
    else:
        return render(request, 'index.html',{'code': 400, 'error': 'username or password error!'})


def event_manage(request):
    return render(request, 'event_manage.html')