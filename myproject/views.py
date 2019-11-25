from django.shortcuts import render,redirect
from . models import *
from .forms import ProjectUpload
from django.contrib.auth.decorators import login_required

def home(request):
    projects = Post.objects.all()
    return render(request,'myprojects/index.html',{"projects":projects})

    
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectUpload(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('home')
    else:
        form = ProjectUpload()
        return render(request,'myprojects/new_post.html',{"form":form})