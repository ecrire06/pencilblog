from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
  email = forms.EmailField()

  class Meta:
      model = User
      fields = ['username', 'password1', 'password2', 'email']

#  def clean(self):
#      cleaned_data = super(UserCreationForm, self).clean()
#      password = cleaned_data.get("password1")
#        # get password from model instance
#      confirm_password = cleaned_data.get("password2")

#      if password != confirm_password:
#          raise forms.ValidationError(
#              "비밀번호가 불일치합니다."
#          )