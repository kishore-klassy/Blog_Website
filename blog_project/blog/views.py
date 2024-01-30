# views.py
from django.shortcuts import redirect, render
from .forms import CreatePostForm, SignUpForm
from .models import Post
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', context={'posts': posts})

def about(request):
    return render(request, 'blog/about.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the desired page after successful registration
            return redirect('blog-home')
    else:
        form = SignUpForm()

    return render(request, 'blog/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # User is authenticated, log them in
                login(request, user)
                # Redirect to the desired page after successful login
                return redirect('blog-home')
            else:
                # Authentication failed, show an error
                form.add_error(None, 'Invalid login credentials. Please try again.')

    else:
        form = AuthenticationForm()

    return render(request, 'blog/login.html', {'form': form})

def create_post(request):
    
    if request.method == 'POST' :
        form = CreatePostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            new_post = Post.objects.create(title=title, content=content, author=request.user)
            new_post.save()
            return redirect('blog-home')
    else :
        form = CreatePostForm()
        return render(request,'blog/createpost.html',{'form':form})
