from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:detail', post.pk)

    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context)


@login_required
def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    context = {
        'post': post,
    }
    return render(request, 'posts/detail.html', context)


@login_required
def answer(request, post_pk, answer):
    post = Post.objects.get(pk=post_pk)
    user = request.user
    if request.method == "POST":
        if user in post.select1_users.all() or user in post.select2_users.all():
            pass
        else:
            if answer == post.select1_content:
                post.select1_users.add(user)
            elif answer == post.select2_content:
                post.select2_users.add(user)
    return redirect('posts:detail', post_pk)

@login_required
def comment_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comment_post_form = Comment_postForm(request.POST)
    if comment_form.is_valid():
        comment_post = comment_post_form.save(commit=False)
        comment_post.user = request.user
        comment_post.post = post
        comment_post.save()

    return redirect('posts:detail', post.pk)


@login_required
def comment_delete(request, post_pk, comment_post_pk):
    comment_post = Comment_post.objects.get(pk=comment_post_pk)
    if request.user == comment_post.user:
        comment_post.delete()

    return redirect('posts:detail', post_pk)


@login_required
def likes(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if post.like_users.filter(pk=request.user.pk).exists():
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
    return redirect('posts:index')


@login_required
def emotes(request, post_pk, emotion):
    post = Post.objects.get(pk=post_pk)
    filter_query = Emote.objects.filter(
        post=post,
        user=request.user,
        emotion=emotion,
    )
    if filter_query.exists():
        filter_query.delete()
    else:
        Emote.objects.create(post=post, user=request.user, emotion=emotion)

    return redirect('posts:detail', post_pk)

@login_required
def comment_likes(request, post_pk, comment_post_pk):
    comment_post = Comment_post.objects.get(pk=comment_post_pk)
    if request.user in comment_post.like_users.all():
        comment_post.like_users.remove(request.user)
    else:
        comment_post.like_users.add(request.user)
    return redirect('posts:detail', post_pk)