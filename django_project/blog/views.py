from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DeleteView
# Create your views here.

# posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 28, 2018'
#     }
# ]


def home(request):
    # return HttpResponse('<h1>Blog Home</h1>')
    context = {
        # 'posts': posts
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DeleteView):
    model = Post


def about(request):
    # return HttpResponse("<h1>Blog About</h1>")
    return render(request, 'blog/about.html', {"title": "About"})
