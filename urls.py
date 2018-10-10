"""jdpay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from djangoapps.pay import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/jdpay/notify/$', views.NotifyViewset.as_view()),
    url(r'^test/jdpay/refund/$', views.refund, name="refund"),
    url(r'^test/jdpay/revoke/$', views.revoke, name="revoke"),
    url(r'^test/jdpay/refund/notify/$', views.refund_notify, name="refund_notify"),
    url(r'^test/jdpay/pay_res/$', views.RedirectViewset.as_view()),
    url(r'^$', views.index),
]
