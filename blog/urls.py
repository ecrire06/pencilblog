from .views import PostListView, PostDetailView, archives, blog, demo, about, changelog
from django.urls import path

urlpatterns = [
  path('', PostListView.as_view(), name='home'),
  path('post/<int:pk>', PostDetailView.as_view(), name='single'),
  path('archives/', archives, name='archives'),
  path('blog/', blog, name='blog'),
  path('demo/', demo, name='demo'),
  path('about/', about, name='about'),
  path('changelog/', changelog, name='changelog'),
]