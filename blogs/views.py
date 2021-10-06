from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import blogs
from django.contrib.auth.models import User,auth
from django.urls import reverse

# Create your views here.
def create_view(request):
    if request.method=='POST':
        title=request.POST['title']
        content=request.POST['content']
        print(title,content)
        user = User.objects.get(username=request.user.username)
        blogs.objects.create(
            title=title,
            content=content,
            user_profile=user
        )
        return HttpResponse('')


def home(request):
    return render(request,'create_post.html')

def show_post(request):
    posts=blogs.objects.all().order_by('created_at')
    # print(posts[0].title)
    # posts=[i for i in range(15)]
    return render(request,'show_post.html',{'posts':posts})

def result_like(request):
    posts = blogs.objects.all().order_by('created_at')
    if request.method == 'POST':
        x=request.POST['id']

        id=blogs.objects.get(id=x)
        id.likes.add(request.user)
        try:
            id.dislikes.remove(request.user)
        finally:
            print(id.dislikes.count())
    return render(request,'show_post.html',{'posts':posts})

def result_dislike(request):
    print('hy')
    if request.method == 'POST':
        x=request.POST['id']

        id=blogs.objects.get(id=x)
        id.dislikes.add(request.user)
        try:
            id.likes.remove(request.user)
        finally:
            print(id.dislikes.count())
        print(id.dislikes.count())
    return render(request,'show_post.html')