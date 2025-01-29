# Create your views here.

from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Blog


def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken!")
        

        # Check if the email already exists
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")

        # Check if the passwords match
        elif password != confirm_password:
            messages.error(request, "Passwords do not match!")

        # Create the new user if all checks pass
        else:
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('index')
        else:
            # Check if the username already exists
            messages.error(request, "Incorrect username or password!")
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

@login_required
def create_blog(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES.get('image')  # Use get() to handle optional uploads
        blog = Blog.objects.create(title=title, content=content, image=image, author=request.user)
        return redirect('index')
    return render(request, 'create_blog.html')

@login_required
def my_blogs(request):
    user_blogs = Blog.objects.filter(author=request.user)  # Filter blogs by logged-in user
    return render(request, 'my_blogs.html', {'blogs': user_blogs})

@login_required
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if blog.author != request.user:
        return redirect('index')
    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.content = request.POST['content']
        if 'image' in request.FILES:
            blog.image = request.FILES['image']
        blog.save()
        return redirect('index')
    return render(request, 'edit_blog.html', {'blog': blog})


def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)  # Fetch the blog post by ID
    return render(request, 'blog_detail.html', {'blog': blog})

@login_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if blog.author == request.user:
        blog.delete()
    return redirect('index')
