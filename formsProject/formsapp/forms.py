from django import forms

class FormName(forms.Form):
    fname= forms.CharField(max_length=100)
    lname= forms.CharField(max_length=100)
    email= forms.EmailField()
    text= forms.CharField(widget=forms.Textarea)
