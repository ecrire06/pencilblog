# ===========DJANGO RELATED==================
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

# ============CUSTOM MADE===============
from .models import Post
from .forms import PostForm
from search_views.search import SearchListView
from search_views.filters import BaseFilter

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

class PostCreateView(LoginRequiredMixin, generic.CreateView):
  form_class = PostForm
  template_name = 'new.html'
  success_url = reverse_lazy('home')

  login_url = 'login'
  redirect_field_name = 'main'
  
  def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
  model = Post
  form_class = PostForm
  template_name = 'new.html'
  success_url = reverse_lazy('home')

  login_url = 'login'
  redirect_field_name = 'main'
  
  def get_queryset(self):
        author = self.request.user
        return self.model.objects.filter(author=author)

class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
  model = Post
  template_name = "delete.html"
  success_url = reverse_lazy("home")

  login_url = 'login'
  redirect_field_name = 'main'

  def get_queryset(self):
        author = self.request.user
        return self.model.objects.filter(author=author)

# =============SEARCH=====================
class PostSearchView(generic.ListView):
    model = Post
    context_object_name = 'search_list'
    template_name = 'search.html'
    paginate_by = 4

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(body_editorjs_custom__icontains=query)
        )
        return object_list
    
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

