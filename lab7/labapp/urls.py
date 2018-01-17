from django.conf.urls import url

from . import views
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .models import *
from django.views.generic import DetailView
urlpatterns = [
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^success_authorization_dumb$', views.success_authorization_dumb, name='success_authorization_dumb'),
    url(r'^success_authorization$', views.success_authorization, name='success_authorization'),
    url(r'^authorization/$', views.authorization, name='authorization'),
    url(r'^registration_dumb/$', views.registration_dumb, name='registration_dumb'),
    url(r'^registration_user/$',views.registration_user, name='registration_user'),
    url(r'^teachers/$',views.TeacherList.as_view(),name='teacher_list'),
    url(r'^pulpit/$',views.PulpitList.as_view(),name='pulpit_list'),
    url(r'^graph/$',views.graph,name='graph'),
    url(r'^add_teacher/$', views.add_teacher, name='add_teacher'),
    # url(r'^reviews/$',views.ReviewList.as_view(),name='review_list'),
    url(r'^$', views.index, name='index'),
    url(r'^teachers/(?P<pk>\d+)$', views.teacher_view.as_view(), name='teacher_view'),
    url(r'^pulpit/(?P<pk>\d+)$', views.pulpit_view.as_view(), name='pulpit_view'),
    url(r'^add_membership/(?P<ded_id>[A-Za-z0-9- ]+)/(?P<pulpit_id>[A-Za-z0-9- ]+)$', views.add_membership, name='add_membership')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)