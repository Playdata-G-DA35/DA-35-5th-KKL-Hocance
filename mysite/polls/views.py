from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import Postform
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'polls/index.html')

def board(request):
    post_list = Post.objects.all().order_by('-mod_date')
    context = {'post_list': post_list}
    return render(request, 'polls/board.html', context)

@login_required()
def create(request):
    if request.method == "GET":
        postForm = Postform()
        context = {'postForm':postForm}
            
        return render(request, "polls/create.html",context)
    
    elif request.method =="POST":
        postform = Postform(request.POST)

    if Postform.is_valid():
        post = Postform.save(commit=False)
        post.save()

        return redirect("polls/read/"+str(post.id))
    
def read(request, pk):
    post = Post.objects.get(pk=pk)
    context = {'post': post}
    return render(request, "polls/read.html",context)
    
def delete(request, id):
    posts = Post.objects.get(id=id)
    Post.delete()
    return redirect("polls/list.html")

