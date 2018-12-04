from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url('Consulta',views.Consulta),
    url('Dashboard',views.Dashboard),
]