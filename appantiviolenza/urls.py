from django.contrib import admin
from django.urls import path, include
from .views import home, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.home, name='home'),
    # path('', include('appantiviolenza.urls')),
    path('login/', login.register_view, name='login'),
]