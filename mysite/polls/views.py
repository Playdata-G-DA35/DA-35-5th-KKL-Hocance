from django.shortcuts import render, redirect
from django.http import HttpResponse
from review_upload.models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def board(request):
    review_list = Review.objects.all()[:100]
    context = {'review_list': review_list}
    return render(request, 'polls/board.html', context)


def read(request, pk):
    post = Review.objects.get(pk=pk)
    context = {'review': post}
    return render(request, "polls/read.html",context)
    