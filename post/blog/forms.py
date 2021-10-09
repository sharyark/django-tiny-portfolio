from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm ,UsernameField
from django.contrib.auth.models import User 
from django.forms import fields, widgets
from django.forms.models import ModelForm

from blog.models import Post 

class singup_(UserCreationForm):
    password1 = forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="re password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        # fields = '__all__'
        labels = {'first_name':'FirstName','last_name':'LastName','email':'Email   :  '}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),'first_name':forms.TextInput(attrs={'class':'form-control'}),'last_name':forms.TextInput(attrs={'class':'form-control'})
        ,'email':forms.TextInput(attrs={'class':'form-control'})}
class login_(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=("password"),widget=forms.PasswordInput(attrs={'autofocus':True,'class':'form-control'}))
class editing(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','desc']