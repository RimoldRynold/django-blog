from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    posts = Posts.objects.all()
    return render(request,'index.html',{'posts':posts})

def posts(request,pk):
    posts = Posts.objects.get(id=pk)
    return render(request,'posts.html',{'posts':posts})