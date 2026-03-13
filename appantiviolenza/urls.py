from django.contrib import admin
from django.urls import path
from .views import home, login, operator
from .views import tickets

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.home, name='home'),
    # path('', include('appantiviolenza.urls')),
    path('login/', login.register_view, name='login'),
    path('operator/', operator.operator_view, name='operator_space'),
    path('tickets/', tickets.tickets_view, name='tickets'),
]