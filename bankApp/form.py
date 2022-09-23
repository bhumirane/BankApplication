from dataclasses import fields
from pyexpat import model
from tkinter import Widget
from django import forms
from .models import Bankinfo

class BankForm(forms.ModelForm):
    class Meta:
        model = Bankinfo
        fields = ['bank_id','first_name','middle_name','last_name','address_1','address_2','city','state','zip_code','phone','gender','email','date_of_birth','social_number','passport_no','account_type','nominee_name']
        labels = {
            'bank_id':'Application Number',
            'first_name':'First Name',
            'middle_name':'Middle Name',
            'last_name':'Last Name',
            'address_1':'Address 1',
            'address_2':'Address 2',
            'city':'City',
            'state':'State',
            'zip_code':'Zip Code',
            'phone':'Phone',
            'gender':'Gender',
            'email':'Email',
            'date_of_birth':'Date of Birth',
            'social_number':'Social Number',
            'passport_no':'Passport Number',
            'account_type':'Account Type',
            'nominee_name':'Nominee Name'
        }
        Widgets={
            'bank_id':forms.NumberInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'middle_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'address_1':forms.TextInput(attrs={'class':'form-control'}),
            'address_2':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.TextInput(attrs={'class':'form-control'}),
            'zip_code':forms.NumberInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'gender':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'date_of_birth':forms.TextInput(attrs={'class':'form-control'}),
            'social_number':forms.TextInput(attrs={'class':'form-control'}),
            'passport_no':forms.TextInput(attrs={'class':'form-control'}),
            'account_type':forms.TextInput(attrs={'class':'form-control'}),
            'nominee_name':forms.TextInput(attrs={'class':'form-control'}),
        }