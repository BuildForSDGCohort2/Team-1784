from .models import Contact
from django.forms import ModelForm
from django import forms


class ContactForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
      'class':'form-control mb-3',
      'id':'name',
      'placeholder':'Full name'
      })) 
    email = forms.CharField(required=False,widget=forms.EmailInput(attrs={
         'class':'form-control mb-3',
         'id':'email',
         'placeholder':'Email'
         }))     
    
    message = forms.CharField(label=False,widget=forms.Textarea(
        attrs={

            'class': "form-control mb-3",
            'id': "message",
            'cols': '30',
            'rows': '10',
            'placeholder':'Messages'
        }
    ))
    
    class Meta:
        model = Contact
        fields = '__all__'
        