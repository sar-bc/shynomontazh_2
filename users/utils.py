from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator as \
    token_generator


# def send_email_for_verify(request, user, mail):
#     current_site = get_current_site(request)
#     context = {
#         'user': user,
#         "http": "http://",
#         'domain': current_site.domain,
#         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#         'token': token_generator.make_token(user),
#     }
#     message = render_to_string('users/verify_email.html', context=context)
#     # print(message)
#     email = EmailMessage(
#         'Проверка почты',
#         message,
#         to=[mail],
#     )
#     email.send()

def send_email_for_verify(request, user):
    current_site = get_current_site(request)
    context = {
        'user': user,
        "http": "http://",
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token_generator.make_token(user),
    }
    message = render_to_string('users/verify_email.html', context=context)
    # print(message)
    email = EmailMessage(
        'Проверка почты',
        message,
        to=[user.email],
    )
    email.send()
