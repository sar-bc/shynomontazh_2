from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.views import View
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from users.utils import send_email_for_verify
from users.forms import UserCreationForm, EditUserForm, EditPhone
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.utils.http import urlsafe_base64_decode
from django.template.loader import render_to_string
from django.urls import reverse
from users.forms import *
from django.contrib.auth.forms import PasswordChangeForm
import re

User = get_user_model()


# ==========================

# =================
class EmailVerify(View):

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('home')
        return redirect('users:invalid_verify')

    @staticmethod
    def get_user(uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError,
                User.DoesNotExist, ValidationError):
            user = None
        return user


# ======================
class LoginAjaxView(View):

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            check_email = User.objects.get(email=email)
            # print(f"check_email:{check_email.email_verify}")
            if user:
                if check_email.email_verify:
                    login(request, user)
                    return JsonResponse(
                        data={
                            'status': 201
                        },
                        status=200
                    )
                return JsonResponse(
                    data={
                        'status': 400,
                        'error': 'Email адрес не подтвержден, проверьте почту'
                    },
                    status=200
                )
            return JsonResponse(
                data={
                    'status': 400,
                    'error': 'Неверный Логин или Пароль'
                },
                status=200
            )
        return JsonResponse(
            data={
                'status': 400,
                'error': 'Введите логин и пароль'
            },
            status=200
        )


###############################################################

###############################################################
class RegisterAjaxView(View):

    def post(self, request):
        form = RegisterAjaxForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(email=request.POST.get('email'), password=request.POST.get('password1'))
            if user:
                # send_email_for_verify(request, request.user, request.POST.get('email'))
                login(request, user)
                send_email_for_verify(request, user)
                logout(request)
                return JsonResponse(data={'status': 201, 'response': 'Для подтверждения регистрации, проверьте почту.'},
                                    status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse(data={'status': 400, 'error': errors}, status=200)

        return JsonResponse(data={'status': 400, 'error': 'Ошибка'}, status=200)


###############################################################
# def logout_user(request):
#     if request.GET:
#         logout(request)
#     return redirect('home')
###################################################

class UserProfile(LoginRequiredMixin, View):
    login_url = '/'
    template_name = 'users/profile.html'
    model = User

    def get(self, request):
        data_user = get_object_or_404(User, email=request.user.email)
        form_user = EditUserForm(data=data_user.username)
        form = EditProfile(data=data_user)
        form_password = ChangeForm(user=request.user)
        # print(data_user.phone)
        form_phone = EditPhone(data=data_user.phone)
        context = {
            'title': 'Личный кабинет',
            'data_user': data_user,
            'form': form,
            'form_phone': form_phone,
            'form_password': form_password,
            'form_user': form_user,

        }
        return render(request, self.template_name, context)

    def post(self, request):
        print(request.POST)

        return render(request, self.template_name, {})


#########################################################
class ChangePasswordAjax(View):
    model = User

    def post(self, request):
        form_password = PasswordChangeForm(user=request.user, data=request.POST)
        if form_password.is_valid():
            form_password.save()
            return JsonResponse(data={'status': 201, 'response': "Успешно, войдите заново!"}, status=200)

        errors = form_password.errors.as_json()
        return JsonResponse(data={'status': 400, 'error': errors}, status=200)

    #########################################################


class EditUserAjax(View):
    # model = User
    def post(self, request):
        if 3 < len(request.POST.get('username')) < 30:
            # form_user = EditUserForm(request.POST)
            # if form_user.is_val?id():
            # form_user.save()
            User.objects.filter(email=request.user.email).update(username=request.POST.get('username'))
            return JsonResponse(data={'status': 201, 'response': 'Успешно'}, status=200)

        # errors = form_user.errors.as_json()
        return JsonResponse(data={'status': 400, 'error': 'Имя слишком короткое или длинное'}, status=200)
    # class EditUserAjax(View):


#     # model = User
#     def post(self, request):
#         form_user = EditUserForm(request.POST)
#         if form_user.is_valid():
#             # form_user.save()
#             User.objects.filter(email=request.user.email).update(username=request.POST.get('username'))
#             return JsonResponse(data={'status': 201},status=200)

#         errors = form_user.errors.as_json()
#         return JsonResponse(data={'status': 400, 'error': errors},status=200)
#########################################################
class EditPhoneAjax(View):
    def post(self, request):
        # form_phone = EditPhone(request.POST)
        reg = "^[+]{1}7 [(]{1}[0-9]{3}[)]{1} [0-9]{3} [0-9]{4}$"
        check_num = re.search(reg, request.POST.get('phone'))
        if check_num:
            User.objects.filter(email=request.user.email).update(phone=request.POST.get('phone'))
            return JsonResponse(data={'status': 201, 'response': 'Успешно'}, status=200)

        return JsonResponse(data={'status': 400, 'error': "Проверьте правильность номера"}, status=200)
#########################################################
