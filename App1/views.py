from App1.models import Contact, Profile,Blog
from django.contrib.auth import models
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        user=User.objects.all()
        user=user[len(user)-5:len(user)]  # slicing the last 5 Username
        context={
            'username':reversed(user)   #slicing last 6 user from the Username
        }
        print(context)
        return render(request,'App1/index.html',context)
    else:
        return redirect('login')

def contact(request):
    if request.method =="POST":
        name =request.POST['name']
        email =request.POST['email']
        subject =request.POST['subject']
        phone =request.POST['number']
        message =request.POST['message']
        if len(phone)>10 & len(phone)<10:
            message.error(request,"PLease Enter the 10 digit of Your Mobile Number")
            return redirect('contact')
        else:
            contact=Contact(name=name,email=email,subject=subject,phone=phone,message=message)
            contact.save()
            messages.success(request,"Thanks For Your Feedback")
            return redirect('index')
    return render(request,'App1/contact.html')

def signup(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        print(username,email,fname,lname,pass1,pass2)
        # check for errorneous input

        if pass1 != pass2:
            messages.error(request,"Password Does Not Match")
            return redirect("signup")
        elif User.objects.filter(username = username).first():
            messages.error(request, "This username is already taken")
            return redirect('signup')
        else:
        # Create the user
            myuser = User.objects.create_user(username=username, email=email, password=pass1)
            myuser.first_name= fname
            myuser.last_name= lname
            myuser.save()
            messages.success(request, " Your Account has been successfully created")
            return redirect('proceed')

    return render(request,'App1/signup.html')

def Login(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user= authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect("index")
        else:
            messages.error(request,"Invalid Credentials")
            return redirect("login")
    return render(request,'App1/login.html')

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login")


def member(request):
    return render(request,'App1/members.html')

def proceed(request):
    if request.method=="POST":
        gender =request.POST['gender']
        lookingFor =request.POST['lookingforgender']
        age =request.POST['age']
        phone =request.POST['phone']

        if phone.isnumeric() and len(phone)==10:
            print("This is if before part ")
            profile =Profile(user=request.user,gender=gender,lookingFor=lookingFor,age=age,phone=phone) 
            messages.success(request,"Your Match has been Successfully Matched!!")
            print("This is if after part ")
            print(request.user,gender)
            profile.save()
            return redirect("index")
        else:
            messages.error(request,"Please Make Sure that phone number is numberic and it must of 10 digit!!")
            
        
   
    return render(request,'App1/proceed.html')

def profile(request):

    return render(request,'App1/profile.html')



def blog(request):
    posts=Blog.objects.all().order_by('-posted_date')
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'App1/blog.html', context)



def post(request, post_id=None):
    post=get_object_or_404(Blog,id=post_id)
    context={
        'post':post
        }        
    return render(request, 'App1/post.html',context)