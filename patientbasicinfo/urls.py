from django.conf.urls import url
from django.urls import path, include

from patientbasicinfo import views

app_name = 'pbi'
urlpatterns = [
    url(r'^$', views.ok, name='ok'),
    url(r'^new_patient/identity/$', views.new_identity, name='new_identity'),
    url(r'^(?P<p_id>[0-9]+)/edit_identity/$', views.edit_identity, name='edit_identity'),
]
