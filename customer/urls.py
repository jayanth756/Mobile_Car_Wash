from django.urls import path
from .views import student,quick_appointmnet,appointment_book



urlpatterns = [
    path('', student, name='student'),
    path('my_appointment/', student, name='student'),
    path('quick_appointmnet/', quick_appointmnet, name='quick_appointmnet'),
    path('update/<int:id>/', appointment_book,name='appointment_update'),
      
]
