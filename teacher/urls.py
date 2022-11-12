from django.urls import path
from .views import teacher,teacher_appointment_list,appointment_delete,teacher_appointment_update


from django.contrib import admin





urlpatterns = [
    path('', teacher, name='teacher_home'),
    path('my_appointment/', teacher, name='teacher_appointment'),
    path('create_appointment/', teacher_appointment_list, name='teacher_appointment_list'),
    path('create_appointment/delete/<int:id>/', appointment_delete,name='appointment_delete'),
    path('create_appointment/update/<int:id>/', teacher_appointment_update,name='teacher_appointment_update'),      
      
]

