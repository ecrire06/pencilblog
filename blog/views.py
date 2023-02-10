from django.views import generic
from .models import Post


class PostListView(generic.ListView):
    context_object_name = 'post_list'
    template_name = 'index.html'
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.all().order_by('-created_date')

class PostDetailView(generic.DetailView):
  model = Post
  template_name = 'single.html'
  