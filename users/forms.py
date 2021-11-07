from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['password1'].help_text = ''
    self.fields['password2'].help_text = ''
  email = forms.EmailField(max_length=200, required=True, help_text='(Required)')
  class Meta:
    model = User
    fields  = ['username', 'first_name' ,'email', 'password1', 'password2']
    help_texts = {'username':''}
  
    def __str__(self):
      return self.first_name