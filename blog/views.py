from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Post #here . means current directory (i.e. blog.models )
from django.utils import timezone
from .forms import PostForm
# Create your views here.

def index(request):
    return HttpResponse("Hello world! <br/> <a href='/about2/'>About2</a><br/><a href='/posts/'>Published Posts</a>")

def index1(request):
    context_dict ={'babaji': "I am rocking dude."}
    return render(request, 'blog/post_default.html', context_dict)

def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    context_dict={'posts' : posts}
    return render(request,'blog/post_list.html', context_dict)

def post_detail(request,pk):
    post=get_object_or_404(Post, pk=pk)
    return render(request,'blog/post_detail.html',{'post': post})

def post_new(request):
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post =form.save(commit=False)
            post.author=request.user
            post.save()

            return redirect('blog.views.post_detail',pk=post.pk)
    else:
        form=PostForm()

    return render(request,'blog/post_edit.html',{'form':form})



def post_edit(request,pk=post.pk):
    form=get_object_or_404(Post,pk=pk)
    if request.method=="POST":
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('blog.views.post_detail',pk=post.pk)

        else:
            form=PostForm(instance=post)

    return render(request, 'blog/post_edit.html',{'form':form})