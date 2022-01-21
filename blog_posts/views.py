from django.shortcuts import redirect, render, HttpResponseRedirect
from . forms import CreatePostForm,UpdatePostForm
from .models import Post


def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'blog_posts/index.html',context)


def detail(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post':post
    }
    return render(request, 'blog_posts/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('index')
    else:
        form = CreatePostForm()
    context = {
        'form':form,
    }
    return render(request, 'blog_posts/create.html', context)

def update(request,id):
    post = Post.objects.get(id=id)
    form = UpdatePostForm(request.POST or None, instance = post)
    if form.is_valid():
       form.save()
       return HttpResponseRedirect("/")
    context = {
        'form':form,
        'post':post
    }
    return render(request,'blog_posts/update.html', context)

def delete(request,id):
    post = Post.objects.get(id=id)
    if request.method =='POST':
        post.delete()
        return HttpResponseRedirect("/")
    return render(request, 'blog_posts/delete.html', {'post':post})

def comments(request,id):
    return render(request,'blog_post/comments.html',context)