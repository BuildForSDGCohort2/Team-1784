from .models import Donor,Grievance, RegularUser, Starred,Type_choice
from users.models import User
from django.forms import ModelForm
from django import forms
from froala_editor.widgets import FroalaEditor


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
    show_info = forms.BooleanField(required=False,label="keep my info public")
    always_show_info = forms.BooleanField(required=False,label="Always keep my info public")
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
        exclude =('user','selected')
    
class GrievanceForm(ModelForm):
    title = forms.CharField(label=False, widget=forms.TextInput(attrs={
        'class':'form-control mb-3',
        'placeholder':'Title'
        }))

    body = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = Grievance
        exclude = ('regular_user',)