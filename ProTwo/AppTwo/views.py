from django.shortcuts import render
from AppTwo.forms import NewUserForm
# from django.http import HttpResponse
# from AppTwo.models import User
# Create your views here.

def index(request):
    # return HttpResponse("<em>My Second App</em>")
    return render(request,"indext.html")

# def help(request):
#     my_dict={'insert_here':'this is from help page'}
#     return render(request,'indext.html',context=my_dict)

def user(request):
    # userlist= User.objects.order_by('first_name')
    # user_dict={'enterhere':userlist}
    # return render(request,'indext.html',context=user_dict)
    form= NewUserForm()
    if request.method=='POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else: print("ERROR OCCURRED")

    return render(request,'user.html',{'form':form})
