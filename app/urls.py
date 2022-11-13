
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('adminapp/', admin.site.urls),
    path('', include("login.urls")),
    path('student/', include("customer.urls")),
    path('teacher/', include("adminapp.urls")),
]
