# ===========DJANGO RELATED==================
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin
from django.db.models import Q
from django.shortcuts import render

# ============CUSTOM MADE===============
from .models import Post
from .forms import PostForm, CommentForm
from search_views.search import SearchListView
from search_views.filters import BaseFilter
from hitcount.views import HitCountDetailView
from next_prev import next_in_order, prev_in_order

# =============POST RELATED CLASS BASED VIEWS==============

class PostListView(generic.ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'home.html'
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.all().order_by('-created_date')

class PostDetailView(HitCountDetailView):
  model = Post
  template_name = 'single.html'
  count_hit = True

  def get_context_data(self, **kwargs):
      context   = super().get_context_data(**kwargs)      
      query_set = Post.objects.all()
      now = self.object
      context['next'] = next_in_order(now)
      context['previous'] = prev_in_order(now, loop=True)
      context['form'] = CommentForm()
      return context

  def post(self, request, *args, **kwargs):
        view = PostComment.as_view()
        return view(request, *args, **kwargs)


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

# ==============TAGGED=======================
class TaggedPostView(generic.ListView):
  model = Post
  context_object_name = 'tagged_list'
  template_name = 'tagged.html'
  paginate_by = 4

  def get_queryset(self):
      return Post.objects.filter(tags__name=self.kwargs['tag'])

# ===========COMMENT======================
class PostComment(SingleObjectMixin, generic.FormView):
    model = Post
    form_class = CommentForm
    template_name = 'single.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(PostComment, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.name = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse('single', kwargs={'pk': post.pk})
  
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

