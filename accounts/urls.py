from django.conf.urls import url
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, \
    password_reset_complete
from django.urls import path, include

from accounts import views

# app_name = 'accounts'
from accounts.patientdetails import view_patientdetails

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='mylogin'),
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}, name='mylogout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^profile/change_password/$', views.change_password, name='change_password'),
    url(r'^reset-password/$', password_reset, name='reset_password'),
    url(r'^reset-password/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\]+)/(?P<token>[0-9A-Za-z]{1,13}[0-9A-Za-z]{1,20})/$',
        password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete, name='password_reset_complete'),
    url(r'^(?P<p_id>[0-9]+)/view_patientdetails/$', view_patientdetails, name='view_patientdetails'),
    # url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(P?<token>.+)$', password_reset_confirm,
    #    name='password_reset_confirm'),

    url(r'^doctorinfo/$', views.view_doctorinfo, name='view_doctorinfo'),
    url(r'^doctorinfo/edit/$', views.edit_doctorinfo, name='edit_doctorinfo'),
    url(r'^doctorinfo/new/$', views.new_doctorinfo, name='new_doctorinfo'),

]
