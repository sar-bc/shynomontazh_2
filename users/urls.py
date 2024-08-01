from django.urls import path, include
from django.views.generic import TemplateView
from . import views

app_name = "users"

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('login_ajax/', views.LoginAjaxView.as_view(), name='login_ajax'),
    # path('logout/', logout_user, name='logout'),
    path('register_ajax/', views.RegisterAjaxView.as_view(), name='register'),
    path('confirm_email/', TemplateView.as_view(template_name='users/confirm_email.html'),
         name='confirm_email'),
    path('verify_email/<uidb64>/<token>/', views.EmailVerify.as_view(), name='verify_email'),
    path('invalid_verify/', TemplateView.as_view(template_name='users/invalid_verify.html'),
         name='invalid_verify'),
    path('profile/', views.UserProfile.as_view(), name='profile'),
    path('password_change_ajax/', views.ChangePasswordAjax.as_view(), name='password_change_ajax'),
    path('edit_user_ajax/', views.EditUserAjax.as_view(), name='edit_user_ajax'),
    path('edit_phone_ajax/', views.EditPhoneAjax.as_view(), name='edit_phone_ajax'),

]
