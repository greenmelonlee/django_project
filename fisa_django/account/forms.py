from django import forms
# Create your views here.

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) # text를 받되 **** 처리
