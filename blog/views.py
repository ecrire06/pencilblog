from django.urls import reverse_lazy
from django.views import generic
from .models import Post
from .forms import PostForm

from django.shortcuts import render

# =============POST RELATED CLASS BASED VIEWS==============

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

class PostCreateView(generic.CreateView):
  form_class = PostForm
  template_name = 'new.html'
  success_url = reverse_lazy('home')

class PostUpdateView(generic.UpdateView):
  model = Post
  form_class = PostForm
  template_name = 'new.html'
  success_url = reverse_lazy('home')

class PostDeleteView(generic.DeleteView):
  model = Post
  template_name = "delete.html"
  success_url = reverse_lazy("home")

# ===============FUNCTION BASED VIEWS=====================
# =========JUST FOR SIMPLE LINK FOR TEMPLATES==============

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

