from django.conf.urls import url
from django.urls import path, include

from patientbasicinfo import views, treatmentplan

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
    url(r'^uploadfile/(?P<p_id>[0-9]+)/$', views.upload_handler, name='upload_handler'),
    url(r'^delete_propic/(?P<p_id>[0-9]+)/$', views.delete_propic, name='delete_propic'),
    url(r'^change_propic/(?P<p_id>[0-9]+)/$', views.change_propic, name='change_propic'),
    #
    url(r'^(?P<p_id>[0-9]+)/new_treatmentplan/$', views.new_treatmentplan, name='new_treatmentplan'),
    url(r'^view_treatmentplan/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/$', treatmentplan.view_treatmentplan,
        name='view_treatmentplan'),
    url(r'^delete/treatmentplan/(?P<p_id>[0-9]+)/(?P<number>[0-9]+)/$', views.delete_treatmentplan,
        name='delete_treatmentplan'),
    #
    url(r'^(?P<p_id>[0-9]+)/(?P<number>[0-9]+)/edit_prescription/$', views.edit_prescription, name='edit_prescription'),
    url(r'^(?P<p_id>[0-9]+)/new_prescription/$', views.new_prescription, name='new_prescription'),
    url(r'^delete/prescription/(?P<p_id>[0-9]+)/(?P<number>[0-9]+)/$', views.delete_prescription,
        name='delete_prescription'),
    #

]
