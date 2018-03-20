from django.conf.urls import url

from targetedtherapy import views

app_name = 'targetedtherapy'


urlpatterns = [
    url(r'^(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/Treatment_plan/immunotherapy/new/$', views.new_immunotherapy,
        name='new_immunotherapy'),
    url(r'^(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/Treatment_plan/immunotherapy/edit/$', views.edit_immunotherapy,
        name='edit_immunotherapy'),

    url(r'^(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/Treatment_plan/tki/new/$', views.new_tki,
        name='new_tki'),
    url(r'^(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/Treatment_plan/tki/edit/$', views.edit_tki,
        name='edit_tki'),

    # url(r'^(?P<p_id>[0-9]+)/Treatment_plan/RadioTherapy/view/$', rtc.view_radiotherapy, name='view_radiotherapy'),
    # url(r'^$', rtc.index, name='radiotherapy_index'),
]