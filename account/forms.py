from django import forms
from django.contrib.auth import views as auth_views

class LoginForm(forms.Form):
    username=forms.CharField(label='用户名',widget=forms.TextInput(attrs={'class': 'form-control'}))
    password=forms.CharField(label='密码',widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegisterForm(forms.Form):
    username=forms.CharField(label='用户名',widget=forms.TextInput(attrs={'class': 'form-control'}))
    password=forms.CharField(label='密码',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    repassword = forms.CharField(label='再次输入密码', widget=forms.PasswordInput(attrs={'class': 'form-control'}))






