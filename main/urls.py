from ast import Index
from django.urls import path, re_path
# from django.views.generic.base import TemplateView
from .views import calendar
from main import views


urlpatterns = [
    # path("robots.txt",TemplateView.as_view(template_name="koleso/robots.txt", content_type="text/plain"),),
    path('', views.index, name='home'),
    path('pages/<slug:id_slug>/', views.pages, name='pages'),
    path('contact/', views.contact, name='contact'),
    path('calendar/', views.calendar, name='calendar'),
    path('api/client/', views.ApiClient.as_view()),
    re_path(r"^api/client/(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2})/$", views.ApiClient.as_view()),
    path('api/client/del/', views.deltime, name='deltime'),
    # re_path(r"^api/client/(?P<year>[0-9]{4})-(?P<month>[0-9]{2})-(?P<day>[0-9]{2})/$", CustAPIView.as_view()),

]