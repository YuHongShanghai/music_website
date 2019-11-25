from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,RegisterForm
from django.http import HttpResponseRedirect,JsonResponse
from django.urls import reverse


def user_login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('song:song_list'))
            else:
                return render(request, 'login.html', {'form': form, 'msg': '用户名或密码错误'})
    else:
        form=LoginForm()
        return render(request,'login.html',{'form':form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('song:song_list'))


def check_user(request):
    username=request.POST['check']
    u = User.objects.get(username=username)
    if u:
        return JsonResponse({'msg':'该用户已存在'})
    return JsonResponse({'msg':''})


def user_register(request):
    if request.method == 'POST':
        if 'check' in request.POST:
            return check_user(request)
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                u = User.objects.create_user(username=cd['username'],password=cd['password'])
                u.save()
                login(request, u)
                return HttpResponseRedirect(reverse('song:song_list'))
            except Exception:
                return render(request, 'register.html', {'form': form,'msg':'注册失败'})

    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})
