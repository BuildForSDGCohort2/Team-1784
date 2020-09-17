from .models import User,UserType,Gender
from django import forms
from django.contrib.auth import authenticate



class LoginForm(forms.Form):
   username = forms.CharField(widget=forms.TextInput(attrs={
      'class':'form-control',
      'id':'login-username',
      "name":"Username",
      'placeholder': 'username or email'
      }))
   password = forms.CharField(widget=forms.PasswordInput(attrs={
      'class':'form-control',
      'id':'login-password',
       'name':'Password',
       'placeholder': 'password'
         
      }))

   def clean(self,*args, **kwargs):
      username = self.cleaned_data.get('username')
      password = self.cleaned_data.get('password')

      if username and password:
         user = authenticate(username=username,password=password)
         if not user:
            raise forms.ValidationError('Incorrect username or password')
         

      return super(LoginForm,self).clean(*args, **kwargs)

# SignUp Form


class SignupForm(forms.ModelForm):

   first_name = forms.CharField(widget=forms.TextInput(attrs={
      'class':'form-control',
      'id':'first_name',
      'placeholder': 'first name'
      
      }))
   last_name = forms.CharField(widget=forms.TextInput(attrs={
      'class':'form-control',
      'id':'last_name',
      'placeholder':'last name'
      }))
   email = forms.CharField(required=False,widget=forms.EmailInput(attrs={
         'class':'form-control',
         'id':'email',
         'placeholder': 'email address'

         
         }))      
   username = forms.CharField(widget=forms.TextInput(attrs={
      'class':'form-control',
      'id':'"username',
      'placeholder':'username'
      
      }))
   phone_number = forms.CharField(widget=forms.TextInput(attrs={
      'class':'form-control',
      'id':'"phone_number',
      'placeholder':'phone number'
      
      }))
   password = forms.CharField(widget=forms.PasswordInput(attrs={
      'class':'form-control',
      'id':'password',
       'name':'password',
       'placeholder': 'password'
         
      }))
   password2 = forms.CharField(widget=forms.PasswordInput(attrs={
      'class':'form-control',
      'id':'password2',
       'name':'password2',
      'placeholder': 'confirm password'
      }))

   userType =forms.ChoiceField(widget=forms.Select(
      attrs={'class':'form-control', 'id':'userType', 'placeholder': 'user type'}
   ), choices=UserType)
   
   gender =forms.ChoiceField(widget=forms.Select(
      attrs={'class':'form-select', 'id':'userType', 'placeholder': 'user type'}
   ), choices=Gender)
  

   
   class Meta:
      model = User
      fields=[
         'first_name',
         'last_name',
         'email',
         'username',    
         'password',
         'password2',
         'userType',
         'gender',
         'profile_picture'
      ]

   def clean(self,*args, **kwargs):
         password = self.cleaned_data.get('password')
         password2 = self.cleaned_data.get('password2')
         email = self.cleaned_data.get('email')
         username = self.cleaned_data.get('username')
         if password != password2:
            raise forms.ValidationError('password not matching')
         if email != '':
            emailqs = User.objects.filter(email=email)
            if emailqs.exists():
               raise forms.ValidationError('Email is already being used')
         usernameqs = User.objects.filter(username=username)
         if usernameqs.exists():
            raise forms.ValidationError('This user name is already being user you can put your email there if only you have one')
         return super(SignupForm,self).clean(*args, **kwargs)
  

class User_profile_picture_Form(forms.ModelForm):
   first_name = forms.CharField(widget=forms.TextInput(attrs={
      'class':'input-material',
      'id':'first_name',
      
      }))
   last_name = forms.CharField(widget=forms.TextInput(attrs={
      'class':'input-material',
      'id':'last_name',
      
      }))
   email = forms.CharField(required=False,widget=forms.EmailInput(attrs={
         'class':'input-material',
         'id':'email',

         
         }))      
   username = forms.CharField(widget=forms.TextInput(attrs={
      'class':'input-material',
      'id':'"username',
      }))


   userType =forms.ChoiceField(widget=forms.Select(
      attrs={'class':'form-control', 'id':'userType'}
   ), choices=UserType)
   
   class Meta:
      model = User
      fields=[
         'first_name',
         'last_name',
         'email',
         'phone_number',
         'username',    
         'userType',
         'profile_picture'
      ]
      def clean(self,*args, **kwargs):
         if email != '':
            emailqs = User.objects.filter(email=email)
            if emailqs.exists():
               raise forms.ValidationError('Email is already being used')
         usernameqs = User.objects.filter(username=username)
         if usernameqs.exists():
            raise forms.ValidationError('This user name is already being user you can put your email there if only you have one')
         return super(SignupForm,self).clean(*args, **kwargs)
  
