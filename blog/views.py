from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
# The dot before models means current directory or current application.
# Both views.py and models.py are in the same directory.
# This means we can use . and the name of the file (without .py).
# Then we import the name of the model (Post).
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()). order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
    


# Please note that we create a variable for our QuerySet: posts.
# Treat this as the name of our QuerySet.
# From now on we can refer to it by this name.
"""
In the render function we have one parameter request (everything we receive
from the user via the Internet) and another giving the template file ('blog/post_list.html').
The last parameter, {}, is a place in which we can add some things for the template to use.
We need to give them names (we will stick to 'posts' right now). :)
It should look like this: {'posts': posts}. Please note that the part before :
is a string; you need to wrap it with quotes: ''.
"""
