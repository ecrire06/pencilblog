from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, archives, blog, demo, about, changelog
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
  
  # =============EDITORJS==============
  path('editorjs/', include('django_editorjs_fields.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)