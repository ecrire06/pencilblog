from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import SignUpView

urlpatterns = [
  path('', LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
  path('logout/', LogoutView.as_view(), name='logout'),
  path('signup/', SignUpView.as_view(), name='signup'),
]