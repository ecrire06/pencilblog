from django.views import generic
from .models import Post

from django.shortcuts import render

# 블로그 Post 관련 View

class PostListView(generic.ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'home.html'
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.all().order_by('-created_date')

class PostDetailView(generic.DetailView):
  model = Post
  template_name = 'single.html'


# 일단 간단히 만들어놓은 View

def archives(request):
  return render(request, 'archives.html')

def blog(request):
  return render(request, 'blog.html')

def demo(request):
  return render(request, 'demo.html')

def about(request):
  return render(request, 'about.html')

def changelog(request):
  return render(request, 'changelog.html')

