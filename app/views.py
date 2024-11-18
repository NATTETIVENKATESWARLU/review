from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from app.forms import *

# Create your views here.
def sample(request):
    return render(request,"index.html")


def movie_review(request):
    movie=movies.objects.all()
    data={"movie":movie}
    return render(request,"movie_review.html",data)


def addlist(request):
    form=movie_add()
    if request.method=="POST":
        form=movie_add(request.POST)
        if form.is_valid:
            form.save()
            return sample(request)
    return render(request,"addlist.html",{"form":form})
    