from django.contrib import admin
from django.urls import path
from .views import home, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.home, name='home'),
    path('login/', login.register, name='register'),
    path('login/', login.login, name='login'),
]