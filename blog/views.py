from django.views import generic
from .models import Post

from django.shortcuts import render

class PostListView(generic.ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'home.html'
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.all().order_by('-created_date')

class PostDetailView(generic.DetailView):
  model = Post
  template_name = 'single.html'

def archives(request):
  return render(request, 'archives.html')

def blog(request):
  return render(request, 'blog.html')

def demo(request):
  return render(request, 'demo.html')

def page(request):
  return render(request, 'page.html')

