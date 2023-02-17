from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostSearchView, TaggedPostView, archives, blog, demo, about, changelog
from django.urls import path, include

# ============EDITORJS============
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', PostListView.as_view(), name='home'),
  path('post/<int:pk>', PostDetailView.as_view(), name='single'),
  path('archives/', archives, name='archives'),
  path('blog/', blog, name='blog'),
  path('demo/', demo, name='demo'),
  path('about/', about, name='about'),
  path('changelog/', changelog, name='changelog'),

  path('new/', PostCreateView.as_view(), name='new'),
  path('update/<int:pk>', PostUpdateView.as_view(), name="update"),
  path('delete/<int:pk>', PostDeleteView.as_view(), name="delete"),

  # ============SEARCH===============
  path('search/', PostSearchView.as_view(), name='search_results'),

  # =============TAGGED===================
  path('tag/<str:tag>', TaggedPostView.as_view(), name='tagged-post'),
  
  # =============EDITORJS==============
  path('editorjs/', include('django_editorjs_fields.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)