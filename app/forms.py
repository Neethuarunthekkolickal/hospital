from django import forms
from . models import Hospital
from django.forms import TextInput, EmailInput, DateInput, TimeInput, Textarea, Select

class HospitalForm(forms.ModelForm):
    class Meta:
        model=Hospital
        fields=['name','email','phone','doctor','date','time','problem']
        widgets = {
            'name':TextInput(attrs={
                "type":"text",
                "class":"form-control border-0",
                "placeholder":"Your Name",
                "style":"height: 55px;"
            }),
            'email':TextInput(attrs={
                "type":"email",
                "class":"form-control border-0",
                "placeholder":"Your Email",
                "style":"height: 55px;"
            }),
            'phone':TextInput(attrs={
                "type":"text",
                "class":"form-control border-0",
                "placeholder":"Your Phone",
                "style":"height: 55px;"
            }),
            'doctor':Select(attrs={
                "class":"form-control border-0",
                "style":"height: 55px; background-color:white"
            }),
            'date':TextInput(attrs={
                "type":"date",
                "class":"form-control border-0",
                "style":"height: 55px;"
            }),
            'time':TextInput(attrs={
                "type":"time",
                "class":"form-control border-0",
                "style":"height: 55px;"
            }),
            'problem':Textarea(attrs={
                "type":"textara",
                "class":"form-control border-0",
                "placeholder":"Describe your problem",
                "rows":"5"
            })
        }