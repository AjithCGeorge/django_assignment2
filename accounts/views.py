from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import profiles

# Create your views here.

def home(request):
    return render(request,'home.html')

def signup_view(request):

    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password1=request.POST['pswd1']
        password2=request.POST['pswd2']
        user_name=request.POST['user_name']
        print(first_name,last_name,email,password1,password2,user_name)
        if password1==password2:
            if User.objects.filter(username=user_name).exists():
                print('user name taken')
                messages.warning(request,'Username already taken')
            elif User.objects.filter(email=email).exists():
                messages.warning(request,'Email id alredy exists')
                print('Email exists')
                return render(request,'register.html')
            else:
                user=User.objects.create_user(username=user_name,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()

                print('User created successfully')
                return render(request,'login.html')
    else:
        return render(request,'register.html')

def login_view(request):
    if request.method == 'POST':
        user_name=request.POST['user_name']
        password=request.POST['pswd']
        print(password,user_name)

        user=auth.authenticate(username=user_name,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Username or Password')
            return redirect('login.html')
    else:
        return render(request,'login.html')

def logout_view(request):
    auth.logout(request)
    return redirect('/')

def profile_view(request):
    if request.method == 'POST':
        mobile_no=request.POST['mobile_no']
        place=request.POST['place']
        alt_email=request.POST['alt_email']
        edu=request.POST['edu']
        hobbies=request.POST['hobbies']
        user = User.objects.get(username=request.user.username)
        # print(mobile_no,place,alt_email,edu,hobbies,request.user.username,user)
        profile=profiles(mobile_num=mobile_no,residence=place,email_alt=alt_email,education=edu,hobbies=hobbies,profile_user=user)
        for i in request.POST:
            print(i)
            # if len(request.POST[i])>0:

        if profiles.objects.filter(profile_user=user).exists():
            print('user exists')
            profile_edit=profiles.objects.get(profile_user=user)
            print(profile_edit.mobile_num)
            profile_edit.mobile_num=mobile_no
            profile_edit.residence=place
            profile_edit.email_alt=alt_email
            profile_edit.education=edu
            profile_edit.hobbies=hobbies
            profile_edit.save()
            return redirect('/')

        else:
            profile.save()
            return render(request,'profile.html')
    else:
        return render(request,'profile.html')
