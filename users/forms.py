from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import PasswordChangeForm
from .validator_phone import validate_phone_number

User = get_user_model()


class AuthenticationAjaxForm(forms.Form):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                'autocomplete': 'email',
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                'class': 'form-control',
                'id': 'password'
            }
        ),
    )


class RegisterAjaxForm(UserCreationForm):
    username = forms.CharField(
        label=_("Ваше имя"),
        min_length=3,
        max_length=254,
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'email',
                'class': 'form-control'
            })
    )
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(
            attrs={'autocomplete': 'email', 'class': 'form-control'})
    )
    phone = forms.CharField(
        max_length=17,
        validators=[validate_phone_number],
        label='Телефон', widget=forms.TextInput(
            attrs={'type': 'tel', 'id': 'online_phone', 'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control login_input'}))
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control login_input'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "phone")
        # fields = ("username",)


class EditProfile(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        data = kwargs.pop('data', None)
        super(EditProfile, self).__init__(*args, **kwargs)
        if data:
            self.fields['username'] = forms.CharField(label='Имя', widget=forms.TextInput(
                attrs={'class': 'form-control form-value ', 'value': data.username, 'disabled': 'True'}))
            self.fields['phone'] = forms.Field(label='Телефон', widget=forms.TextInput(
                attrs={'type': 'tel', 'id': 'online_phone', 'class': 'form-control',
                       'pattern': '[+]{1}7 [(]{1}[0-9]{3}[)]{1} [0-9]{3} [0-9]{4}', 'value': data.phone,
                       'disabled': 'True'}))
            self.fields['email'] = forms.EmailField(label='E-mail', required=False, widget=forms.TextInput(
                attrs={'class': 'form-control form-value ', 'value': data.email, 'required': 'False',
                       'disabled': 'True'}))
            self.fields['password'] = forms.CharField(label='Пароь', required=False, widget=forms.PasswordInput(
                attrs={'class': 'form-control form-value ', 'value': '0000000000000', 'required': 'False',
                       'disabled': 'True'}))

    class Meta:
        model = User
        fields = ['username', 'phone', 'email']


class EditPhone(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        data = kwargs.pop('data', None)
        super(EditPhone, self).__init__(*args, **kwargs)
        # print(data)
        if data:
            self.fields['phone'] = forms.CharField(label='Телефон', widget=forms.TextInput(
                attrs={'type': 'tel', 'id': 'online_phone', 'class': 'form-control',
                       'pattern': '[+]{1}7 [(]{1}[0-9]{3}[)]{1} [0-9]{3} [0-9]{4}', 'placeholder': '+7 (999) 123 4455',
                       'value': data}))

    class Meta:
        model = get_user_model()
        fields = ['phone']


class ChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control form-value ', 'autocomplete': 'current-password', 'autofocus': True}),
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control form-value ', 'autocomplete': 'new-password', 'autofocus': True})
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control form-value ', 'autocomplete': 'new-password', 'autofocus': True})
    )


class EditUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        data = kwargs.pop('data', None)
        super(EditUserForm, self).__init__(*args, **kwargs)
        # print(data)
        if data:
            self.fields['username'] = forms.CharField(label='Ваше имя', widget=forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'value': data}))

    class Meta:
        model = get_user_model()
        fields = ['username']
