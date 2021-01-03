from django.shortcuts import render
from formsapp import forms
# Create your views here.
def index(response):
    return render(response,"index.html")

def djform(response):
    myform= forms.FormName()
    form_dict={"form":myform}
    return render(response,"forms.html",context=form_dict)
