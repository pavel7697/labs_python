"""lab5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
import polls.views

urlpatterns = [
    url(r'^$', polls.views.OrdersView.as_view(), name='order_url'),
    url(r'^order/(?P<id>\d+)', polls.views.OrderView.as_view(), name='order_url'),
    url(r'^admin/', admin.site.urls),
    url(r'^pvar', polls.views.pvariable),
    url(r'^home', polls.views.base),
]
