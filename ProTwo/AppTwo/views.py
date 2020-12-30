from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
# Create your views here.

def index(request):
    return HttpResponse("<em>My Second App</em>")

# def help(request):
#     my_dict={'insert_here':'this is from help page'}
#     return render(request,'indext.html',context=my_dict)

def user(request):
    userlist= User.objects.order_by('first_name')
    user_dict={'enterhere':userlist}
    return render(request,'indext.html',context=user_dict)
