from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pulpits/', views.Pit, name='pulpit')
    # url(r'^single/', views.Pit, name='pulpit')
]