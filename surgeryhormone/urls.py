from django.conf.urls import url

from surgeryhormone import views

app_name = 'surgeryhormone'


urlpatterns = [
    url(r'^(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/Treatment_plan/Surgery/new/$', views.new_surgery, name='new_surgery'),
    url(r'^(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/Treatment_plan/Surgery/edit/$', views.edit_surgery, name='edit_surgery'),
    url(r'^(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/Treatment_plan/Hormone/new/$', views.new_hormone, name='new_hormone'),
    url(r'^(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/Treatment_plan/Hormone/edit/$', views.edit_hormone, name='edit_hormone'),

    # url(r'^(?P<p_id>[0-9]+)/Treatment_plan/RadioTherapy/view/$', rtc.view_radiotherapy, name='view_radiotherapy'),
    # url(r'^$', rtc.index, name='radiotherapy_index'),
]