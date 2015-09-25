import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from models import Profile
from models import Careers
from models import Exp

from django import forms
from django.core import validators
import pdb
from captcha.fields import CaptchaField
class NameForm(forms.Form):
    name=forms.CharField(max_length=30, min_length=4)
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    surname=forms.CharField(max_length=30, min_length=4)
    phone_number=forms.IntegerField()
   # phone_number = PhoneNumberField()
    ssc=forms.IntegerField()
    inter=forms.IntegerField()
    highest_qualification=forms.CharField(max_length=10)
    #captcha = CaptchaField()
    docfile = forms.FileField(

        label='Select a file',

        help_text='max. 42 megabytes',
        allow_empty_file=True
        
    )

    def clean_name(self):    
        e = self.cleaned_data['name']
        print e
        if not Profile.objects.filter(name=e):
            return e
        else:
            raise forms.ValidationError("name  already exists")

    def clean_email(self):
        e = self.cleaned_data['email']
        print e
        if not Profile.objects.filter(email=e):
            return e
        else:
            raise forms.ValidationError("email  already exists")
   

class CareersForm(forms.Form):
    
     firstname=forms.CharField(max_length=30, min_length=4)
     lastname=forms.CharField(max_length=30, min_length=4)
     email=forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))

     def clean_firstname(self):
        var = self.cleaned_data['firstname']
        print var
        if not Careers.objects.filter(firstname=var):
            return var
        else:
            raise forms.ValidationError("name  already exists")

     def clean_email(self):
        var = self.cleaned_data['email']
        print var
        if not Careers.objects.filter(email=var):
            return var
        else:
            raise forms.ValidationError("email  already exists")

class ExpForm(forms.Form):
    primary=forms.CharField(max_length=30, min_length=4)
    secondary=forms.CharField(max_length=30, min_length=4)
    role=forms.CharField(max_length=30, min_length=4)
    designation=forms.CharField(max_length=30, min_length=4)
    exp=forms.IntegerField()
    ctc=forms.FloatField(required=False,label= "Material Name", widget=forms.TextInput(attrs={'placeholder': 'Material float'}))
    exp_ctc=forms.FloatField(required=False,label= "Material Name", widget=forms.TextInput(attrs={'placeholder': 'Material float'}))
    reason_for_change=forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}))
    current_company=forms.CharField(max_length=100)
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    docfile = forms.FileField(

        label='Select a file',

        help_text='max. 42 megabytes',
        allow_empty_file=True

    )

class PythonForm(forms.Form):
  
    Python=forms.FloatField(required=False,label= "Material Name", widget=forms.TextInput(attrs={'placeholder': 'Material float'}))
    Django=forms.FloatField(required=False,label= "Material Name", widget=forms.TextInput(attrs={'placeholder': 'Material float'}))
    Html=forms.FloatField(required=False,label= "Material Name", widget=forms.TextInput(attrs={'placeholder': 'Material float'}))
    Linux=forms.FloatField(required=False,label= "Material Name", widget=forms.TextInput(attrs={'placeholder': 'Material float'}))
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))

    docfile = forms.FileField(

        label='Select a file',

        help_text='max. 42 megabytes',
        allow_empty_file=True

    )
  
   
    
    



