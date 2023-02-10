from .views import PostListView, PostDetailView
from django.urls import path

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
  path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
]