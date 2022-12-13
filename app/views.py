from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login as loginuser,logout

from app.models import TODO
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
   return render(request, 'index.html')
   

def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            "form" : form
        }
        return render(request,'login.html',context = context)
    else:
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username,password = password)
            print("Authenticated",user)
            if user is not None:
                loginuser(request,user)
                return redirect('home')
            # else:
            #     form = AuthenticationForm()
            #     context = {
            #     "form" : form
            #     }
            #     return render(request,'login.html',context = context)



        else:
            form = AuthenticationForm()
            context = {
            "form" : form
            }
            return render(request,'login.html',context = context)


                    


        


def signup(request):
    if(request.method == 'GET'):
        form = UserCreationForm()
        context = {
            "form": form
        }
        return render(request,'signup.html',context = context)
    else:
        form = UserCreationForm(request.POST)
        context = {
            "form": form
        }
        if form.is_valid():
            # return render(request,'signup.html',context = context)
            user = form.save()
            print(user)
            if user is not None:
                return redirect('home')
        else:
            return render(request,'signup.html',context = context)
 

def signout(request):
    logout(request)
    return redirect('home')


def doctors(request):
    if request.user.is_authenticated:
        user = request.user
        todos = TODO.objects.filter(user=user)
        print(todos[0].user                                                                              )
        return render(request,'doctors.html',context={'todos':todos}) 
    else:
         return render(request,'doctors.html')      




    # return render(request,'signup.html',context = context)