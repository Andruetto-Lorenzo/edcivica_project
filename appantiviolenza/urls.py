from django.contrib import admin
from django.urls import path
from .views import home, login, operator, contacts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.home, name='home'),
    # path('', include('appantiviolenza.urls')),
    path('login/', login.register_view, name='login'),
    path('operator/', operator.operator, name='operator_space'),
    path('contacts/', contacts.contacts, name='contacts'),
]