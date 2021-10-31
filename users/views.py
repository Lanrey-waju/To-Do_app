from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm

# Create your views here.
def register(request):
  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      form.save()
      return redirect('login')

  else:
    form = CreateUserForm()
  return render(request, 'users/register.html', {'form': form})