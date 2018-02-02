
from django.conf.urls import url
from rango import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    #new
    url(r'^about/', views.about, name='about'),
]
