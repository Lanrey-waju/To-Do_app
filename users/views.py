from django.contrib.auth import authenticate, get_user_model, login
from django.shortcuts import redirect, render, HttpResponseRedirect, reverse
from .forms import CreateUserForm
from .token import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.http import HttpResponse

# Create your views here.
def register(request):
  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = form.save(commit=False)
      user.is_active = False
      user.save()
      # Get the domain name of current site
      current_site = get_current_site(request)
      mail_subject = "Activation link hass been sent to your mail"
      message = render_to_string('acc_active-mail.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token(user)
      })
      to_email = form.cleaned_data.get('email')
      email = EmailMessage(mail_subject, message, to=[to_email])
      email.send()
      return redirect('login')

  else:
    form = CreateUserForm()
  return render(request, 'users/register.html', {'form': form})


def activate(uidb64, token):
  User = get_user_model()
  try:
    uid = urlsafe_base64_decode(uidb64)
    user = User.objects.get(pk=uid)
  except(TypeError, ValueError, OverflowError, User.DoesNotExist):
    user = None
  if user is not None and account_activation_token.check_token(user, token):
    user.is_active = True
    user.save()
    return HttpResponse('Email Confirmed. Now you can log in to your account')
  else:
    return HttpResponse('Activation link is invalid')