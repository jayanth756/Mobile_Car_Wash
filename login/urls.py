from django.urls import path
from .views import logout_view,group_check,register_student,register_teacher
from django.contrib.auth.views import LoginView



urlpatterns = [
      path('', LoginView.as_view(template_name='index.html'), name="home"),
      path('logout/', logout_view, name='logout'),
      path('group/', group_check, name='group'),
      path('register_teacher/', register_teacher.as_view(), name='register_teacher'),
      path('register_student/', register_student.as_view(), name='register_student'),
]