from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from .forms import AddMessageForm
from django.http import JsonResponse
from .models import Time, Recording_Time, Page
from django.core.mail import send_mail
from django.conf import settings
from datetime import date, timedelta
from . import utils
import datetime
import re
from django.contrib.auth import get_user_model

User = get_user_model()

date_max = date.today() + timedelta(days=30)


######################################
#########################################################################################
def index(request):
    year = datetime.date.today().year
    context = {
        "title": "Ваш Шиномантаж",
        "year": year,
    }
    return render(request, "main/index.html", context=context)


#########################################################################################,
def pages(request, id_slug):
    year = datetime.date.today().year
    serv = get_object_or_404(Page, slug=id_slug)
    context = {
        'title': serv.title,
        'year': year,
        'content': serv.body
    }
    return render(request, 'main/pages.html', context=context)


#########################################################################################
class ApiClient(View):

    def get(self, request, **kwargs):
        # response to client json format
        # {"date":'2024-04-28', "date_max": '2024-05-28', "time_all":['08:00','08:30',...,'19:00], "time_busy":[]}
        time_all = Time.objects.all()
        time_busy = []
        # print(list(map(str,time_all)))
        if kwargs:
            # print("работаем дальше")
            get_date = kwargs["date"]
            # get_del = kwargs["del"]
            # if kwargs["del"]:
            #     print("удаляем")
            if get_date:
                d = Recording_Time.objects.filter(pub_date__date=get_date).order_by("pub_date").values()
                for i in d:
                    time_busy.append(i['pub_date'].strftime("%H:%M"))
                return JsonResponse(
                    {"date": get_date,
                     "date_max": date_max,
                     "time_all": list(map(str, time_all)),
                     "time_busy": time_busy}
                    , status=200)
        else:
            # use the current date
            # time_busy = []
            d = Recording_Time.objects.filter(pub_date__date=date.today()).order_by("pub_date").values()
            for i in d:
                time_busy.append(i['pub_date'].strftime("%H:%M"))
            return JsonResponse(
                {"date": date.today(),
                 "date_max": date_max,
                 "time_all": list(map(str, time_all)),
                 "time_busy": time_busy}
                , status=200)

    def post(self, request):

        if request.user.username:
            # записываем в бд
            # print(f"Avto:{request.POST.get('avto')}")
            # print(f"Date:{request.POST.get('date')}")
            # print(f"Time:{request.POST.get('time')}")
            post_data = f"{request.POST.get('date')} {request.POST.get('time')}"
            m = Recording_Time.objects.filter(pub_date=post_data)
            # print(len(m))
            if len(m) > 0:
                print("запись есть")
            else:
                # print("записи нет")
                user_id = User.objects.get(id=request.user.id)
                # check_user_time = Recording_Time.objects.filter(pub_date__date=request.POST.get('date'), user_id=user_id).distinct()
                # check_user_time = Recording_Time.objects.filter(user_id=user_id).get(pub_date__date=request.POST.get('date'))
                check_user_time = Recording_Time.objects.all().filter(user_id=user_id,
                                                                      pub_date__date=request.POST.get('date'))

                # print(check_user_time)
                if check_user_time:
                    print(f"check_user_time:{check_user_time}")

                    # s = Recording_Time.objects.get(id=check_user_time.id)
                    s = Recording_Time.objects.filter(user_id=user_id).get(pub_date__date=request.POST.get('date'))
                    s.pub_date = post_data
                    s.count += 1
                    s.save()
                    print("update:", s)
                    return JsonResponse(
                        data={
                            'status': 401,
                            'error': 'Ваше время обновлено!'
                        },
                        status=200
                    )
                else:
                    s = Recording_Time.objects.create(avto=request.POST.get('avto'), pub_date=post_data, user=user_id)
                    print("create:", s)

            return JsonResponse(data={'status': 201}, status=200)
        else:
            return JsonResponse(
                data={
                    'status': 400,
                    'error': 'Для записи, авторизуйтесь'
                },
                status=200
            )

        #########################################################################################


def deltime(request):
    if request.method == 'POST':
        try:
            rec = Recording_Time.objects.filter(id=request.POST.get('del'))
            rec.delete()
            return JsonResponse(data={'status': 201, 'response': 'Успешно'}, status=200)
        except IntegrityError:
            return JsonResponse(data={'status': 400, 'error': 'Ошибка удаления'}, status=200)


#########################################################################################
def calendar(request):
    year = datetime.date.today().year
    m = Recording_Time.objects.filter(user_id=request.user.id).order_by('pub_date')
    context = {
        "title": "Ваш Шиномантаж",
        "year": year,
        "m": m
    }

    return render(request, "main/calendar.html", context=context)


#########################################################################################

def contact(request):
    if request.method == 'POST':
        form = AddMessageForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            x = request.POST.dict()
            form.save()
            mess = "Новое сообщение от " + x.get('name') + "; e-mail: " + x.get('email') + "; Тел: " + x.get(
                'phone') + "; Сообщение: " + x.get('message')
            # print(mess)
            send_mail('Уведомление с сайта Шиномонтаж', mess, settings.EMAIL_HOST_USER,
                      [settings.EMAIL_FROM_ADMIN, settings.EMAIL_FROM_CLIENT], fail_silently=False, )
            return redirect('home')
    else:
        form = AddMessageForm()
    year = datetime.date.today().year
    context = {
        'title': 'Ваш Шиномантаж',
        'form': form,
        'year': year
    }
    return render(request, 'main/contact.html', context=context)


########################################################################################
def pageNotFound(request, exception):
    year = datetime.date.today().year
    context = {
        'title': 'Ваш Шиномантаж',
        'year': year
    }
    return render(request, 'main/page_not_found.html', context=context)
#########################################################################################
