from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields  = ['username', 'first_name' ,'email', 'password1', 'password2']

    def __str__(self):
      return self.first_name