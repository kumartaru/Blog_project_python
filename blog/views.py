from django.shortcuts import render,HttpResponseRedirect
from blog.forms import SignupForm,LoginForm,Postform   
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from blog.models import post
from django.contrib.auth.models import Group
# Create your views here.
def home(request):
    posts=post.objects.all()
    return render(request,'blog/home.html',{'post':posts})

def about(request):
    return render(request,'blog/about.html')


def dashboard(request):
    if request.user.is_authenticated:
        posts=post.objects.all()
        user=request.user
        full_name=user.get_full_name()
        gps=user.groups.all()
        return render(request, 'blog/dashboard.html',{'post':posts,'fullname':full_name,'group':gps})
    else:
        return HttpResponseRedirect('/blog/login/') 


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
    


def sign_up(request):
    if request.method=='POST':
        s = SignupForm(request.POST)
        if s.is_valid():
            messages.success(request,'Your are login')
            user=s.save()
            group=Group.objects.get(name='Author')
            user.groups.add(group)
    else:
       s = SignupForm()

    return render(request, 'blog/signup.html',{'form':s})

# Login 
def user_login(request):
 if not request.user.is_authenticated:
  if request.method == "POST":
   form = LoginForm(request=request, data=request.POST)
   if form.is_valid():
    uname = form.cleaned_data['username']
    upass = form.cleaned_data['password']
    user = authenticate(username=uname, password=upass)
    if user is not None:
     login(request, user)
     messages.success(request, 'Logged in Successfully !!')
     return HttpResponseRedirect('/blog/dashboard/')
  else:
   form = LoginForm()
  return render(request, 'blog/login.html', {'form': form})
 else:
  return HttpResponseRedirect('/blog/dashboard/')


# Add new Post  
def Addpost(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            s=Postform(request.POST)
            if s.is_valid():
                title=s.cleaned_data['title']
                desc=s.cleaned_data['desc']
                pst=post(title=title,desc=desc)
                pst.save()
                s = Postform()
        else:
            s=Postform
        return render(request,'blog/addpost.html',{'form':s})
    else:
        return HttpResponseRedirect('/blog/login/')  

# Update Post
def updatepost(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=post.objects.get(pk=id)
            s=Postform(request.POST,instance=pi)
            if s.is_valid():
                form.save()
        else:
            pi=post.objects.get(pk=id)
            s=Postform()        
        return render(request,'blog/updatepost.html',{'form':s})
    else:
        return HttpResponseRedirect('/blog/login/')


#Delete Post
def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/blog/dashboard/')  
        else:
            return HttpResponseRedirect('/blog/login/')


