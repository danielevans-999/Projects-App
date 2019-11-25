from django.shortcuts import render,redirect

def home(request):
    return redirect('accounts/register')

def projects(request):
    
    return render(request,'myprojects/index.html')