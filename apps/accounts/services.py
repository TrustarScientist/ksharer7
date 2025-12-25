from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth import authenticate, login

from .tokens import account_activation_token

User = get_user_model()


def register_user(form, request):
    user = form.save(commit=False)
    user.is_active = False
    user.save()

    send_activation_email(user, request)
    return user


def send_activation_email(user, request):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = account_activation_token.make_token(user)

    activation_link = request.build_absolute_uri(
        reverse('accounts:activate', args=[uid, token])
    )

    message = (
        "Activate your account\n\n"
        f"{activation_link}\n\n"
        "If you did not request this, ignore this email."
    )

    send_mail(
        subject="Activate your account",
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
    )


def login_user(request, identifier, password):
    user = authenticate(
        request,
        username=identifier,
        password=password
    )

    if not user:
        return None

    if not user.is_active:
        return "inactive"

    login(request, user)
    return user



# old code
# def login_user(request, identifier, password):
#     # user = authenticate(
#     #     request,
#     #     username=identifier,
#     #     password=password
#     # )
#     # if user:
#     #     login(request, user)
#     # return user

#     user = authenticate(
#         request,
#         username=identifier,
#         password=password
#     )
#     if user and user.is_active:
#         login(request, user)
#         return user
#     return None
