from unittest import result
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

User = get_user_model()

from .forms import LoginForm, RegisterForm
from .services import login_user, register_user, account_activation_token

@login_required
def home(request):
    return render(request, 'accounts/home.html')

def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        result = login_user(
            request,
            form.cleaned_data['identifier'],
            form.cleaned_data['password']
        )

        if result == "inactive":
            form.add_error(None, "Please activate your account via email.")
        elif result:
            return redirect('accounts:home')
        else:
            form.add_error(None, "Invalid credentials")

    return render(request, 'accounts/login.html', {'form': form})



def register_view(request):
    form = RegisterForm(request.POST or None)
    print(form.non_field_errors())
    if request.method == 'POST' and form.is_valid():
        register_user(form, request)
        return render(request, 'accounts/register_done.html')
    return render(request, 'accounts/register.html', {'form': form})



def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception:
        user = None

    # print("USER:", user)
    # print("ACTIVE:", user.is_active)
    # print("TOKEN OK:", account_activation_token.check_token(user, token))

    if not user:
        return render(request, 'accounts/activation_invalid.html')

    if user.is_active:
        return render(request, 'accounts/activation_already_done.html')

    if account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('accounts:login')

    return render(request, 'accounts/activation_invalid.html')

