from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Create your views here. 

def post_list(request):
    posts = Post.objects.filter()
    print(posts)
    return render(request, 'myapp/post_list.html', {'posts': posts})