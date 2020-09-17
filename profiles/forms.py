from .models import Donor,Grievance, RegularUser, Starred,Type_choice
from users.models import User
from django.forms import ModelForm
from django import forms


class RegularUserForm(ModelForm):
    country = forms.CharField(label=False,widget=forms.TextInput(attrs={
      'class':'form-control mb-3',
      'id':'name',
      'placeholder':'Country'

      })) 
    region_or_state = forms.CharField(label=False,widget=forms.TextInput(attrs={
      'class':'form-control mb-3',
      'id':'name',
      'placeholder':'Region or State'
      })) 
    city= forms.CharField(label=False,widget=forms.TextInput(attrs={
      'class':'form-control mb-3',
      'id':'name',
      'placeholder':'City'
      })) 
    age = forms.IntegerField(required=False,widget=forms.TextInput(attrs={
         'class':'form-control mb-3',
         'id':'email',
         'placeholder':'Age'
         }))     
    interest = forms.CharField(label=False,widget=forms.TextInput(attrs={
      'class':'form-control mb-3',
      'id':'name',
      'placeholder':'Interest'
      }))   
    education_level = forms.CharField(label=False,widget=forms.TextInput(attrs={
      'class':'form-control mb-3',
      'id':'name',
      'placeholder':'Level of Education'
      })) 
    brief_introduction = forms.CharField(label=False,widget=forms.Textarea(
        attrs={

            'class': "form-control mb-3",
            'cols': '30',
            'rows': '10',
            'placeholder':'Write a brief introduction about you'
        }
    ))
    
    class Meta:
        model = RegularUser 
        exclude =('user',)
    
class DonorForm(ModelForm):
    name = forms.CharField(label=False, widget=forms.TextInput(attrs={
        'class':'form-control mb-3',
        'id':'name',
        'placeholder':'Full name'
        }))
    i_am = forms.CharField(label=False, widget=forms.Select(attrs={
      'class':'form-control mb-3',
      'id':'name',
      }, choices=Type_choice)) 
    class Meta:
        model = Donor
        exclude =('user',)
    
class GrievanceForm(ModelForm):
    talent = forms.CharField(label=False, widget=forms.TextInput(attrs={
        'class':'form-control mb-3',
        'id':'name',
        'placeholder':'What can you do best'
        }))
    help_you_need = forms.CharField(widget=forms.TextInput(attrs={
      'class':'form-control mb-3',
      'id':'name',
      'placeholder':'What help you wish to get'
      })) 
    demo_in_text = forms.CharField(label=False,widget=forms.Textarea({
        'class': 'form-control mb-3',
        'placeholder': 'If your talent can be expressed in text, demo here'
    }))
    class Meta:
        model = Grievance
        exclude = ('regular_user',)