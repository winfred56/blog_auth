from django.shortcuts import redirect, render, HttpResponseRedirect
from .forms import CreatePostForm, UpdatePostForm, CommentForm, UpdateCommentForm
from .models import Post, Comment


def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'blog_posts/index.html',context)


def detail(request, id):
    post = Post.objects.get(id=id)
    comments = post.comments.all()
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            #sets the comment author to the current logged in user
            comment_form.instance.author = request.user
            #Gets the comment but doesn't save in the database yet
            new_comment = comment_form.save(commit=False)
            #assigns the comment to the current post id and saves it
            new_comment.post = post
            new_comment.save()
            #Empty the form
            comment_form  = CommentForm()

    else:
        comment_form = CommentForm()
    context = {
        'post':post,
        'form': comment_form,
        'comments': comments
    }
    return render(request, 'blog_posts/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            #Assigns the author of the post to the current logged in user
            form.instance.author = request.user
            form.save()
            #returns to the post's detail
            return redirect('f/posts/{post.id}')
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
       return redirect(f'/posts/{post.id}') #redirects to post detail view
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


def update_comment(request,id):
    comment = Comment.objects.get(id=id)
    form = UpdateCommentForm(request.POST or None, instance = comment)
    if form.is_valid():
        form.save()

        # redirects to the main post been commented on
        return redirect(f'/posts/{comment.post.id}') 
    context= {'form':form}
    return render(request, 'blog_posts/update_comment.html', context)

def delete_comment(request, id):

    # Gets the id of the selected comment
    comment = Comment.objects.get(id=id) 
    if request.method == 'POST':
        comment.delete()
        # redirects to the main post been commented on
        return redirect(f'/posts/{comment.post.id}')
    context = {'comment':comment}
    return render(request, 'blog_posts/delete_comment.html', context)