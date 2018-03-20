from django.conf.urls import url

from radiotherapy import views

app_name = 'radiotherapy'



urlpatterns = [
    url(r'^Treatment_plan/RadioTherapy/Cobalt/new/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/$', views.new_Cobalt, name='new_Cobalt'),
    url(r'^Treatment_plan/RadioTherapy/Cobalt/edit/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/$', views.edit_Cobalt, name='edit_Cobalt'),

    url(r'^Treatment_plan/RadioTherapy/Linac/new/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/$', views.new_Linac, name='new_Linac'),
    url(r'^Treatment_plan/RadioTherapy/Linac/edit/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/$', views.edit_Linac, name='edit_Linac'),

    url(r'^Treatment_plan/RadioTherapy/Brachy/new/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/$', views.new_Brachy, name='new_Brachy'),
    url(r'^Treatment_plan/RadioTherapy/Brachy/edit/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/$', views.edit_Brachy, name='edit_Brachy'),
]
