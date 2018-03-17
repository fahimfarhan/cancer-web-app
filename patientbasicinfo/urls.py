from django.conf.urls import url
from django.urls import path, include

from patientbasicinfo import views

app_name = 'pbi'
urlpatterns = [
    url(r'^$', views.ok, name='ok'),
    url(r'^new_patient/identity/$', views.new_identity, name='new_identity'),
    url(r'^(?P<p_id>[0-9]+)/edit_identity/$', views.edit_identity, name='edit_identity'),
    #
    url(r'^(?P<p_id>[0-9]+)/edit_comorbidity/$', views.edit_comorbidity, name='edit_comorbidity'),
    url(r'^(?P<p_id>[0-9]+)/new_comorbidity/$', views.new_comorbidity, name='new_comorbidity'),
    #
    url(r'^(?P<p_id>[0-9]+)/edit_profile/$', views.edit_profile, name='edit_profile'),
    url(r'^(?P<p_id>[0-9]+)/new_profile/$', views.new_profile, name='new_profile'),
    #
]
