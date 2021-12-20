from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def loginView(request):
    if request.method == 'POST':
        un=request.POST.get('un')
        pw=request.POST.get('pw')
        print(f"data received from fe,username={un},password={pw}")
        user=authenticate(username=un,password=pw)
        print(f"user={user}")
        if user is not None:
            login(request,user)
            return redirect('show_lap')
        else:
            print('invalid login id or password')
            messages.error(request,'invalid login id or password')
    template_name = 'AuthApp/login.html'
    context = {}
    return render(request, template_name, context)


def registerView(request):
    form=UserCreationForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context={'form':form}
    template_name='AuthApp/register.html'
    return render(request, template_name, context)

def logoutView(request):
    logout(request)
    return redirect('login')