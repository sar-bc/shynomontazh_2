
from django.test import TestCase
# from datetime import date,timedelta
# import datetime

# from .models import Time

# time_all = Time.objects.all()
# for i in time_all:
#     print(i)

# day = datetime().day()
# month =date.month()
# year= date.year()
# today = date.today()


# Create your tests here.
# time_all = [
#     '08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00',
#     '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30',
#     '15:00', '15:30', '16:00', '16:30', '17:00', '17:30',
#     '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30',
#     '22:00', '22:30'
# ]
# time_busy = [
#    '10:00','12:00', '15:00'
# ]
# print(f"Test time:{today}")
# date_max = date.today() + timedelta(days=30)
# print(f"Time MAX: {date_max}")
# print(len(time_all))
# print(round(len(time_all)/4))

# def group_time_slots(t):
#     time_row = []
#     time_group = []
#     for i in t:
#         time_row.append(i)
#         if len(time_row) == 4:
#             time_group.append(time_row)
#             time_row = []
#     if time_row:
#         time_group.append(time_row)

#     return time_group

# print(group_time_slots(time_all))      
      
# time_group = [
#     ['08:00', '08:30', '09:00', '09:30'],
#     ['10:00', '10:30', '11:00', '11:30'],
#     ['12:00', '12:30', '13:00', '13:30'],
#     ['14:00', '14:30','15:00', '15:30'],
#     ['16:00', '16:30', '17:00', '17:30'],
#     ['18:00', '18:30', '19:00']
# ]
# print(time_group)
import re
s = "2024-04-32"
# reg = "^[\d]{4}-[\d]{2}-[\d]{2}$"
reg = "(19[0-9][0-9]|20[0-9][0-9])-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])"
x = re.findall(reg,s)
print(x)

# s = "41-12-2024"
# reg = "(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])"
# print(re.findall(reg, s))