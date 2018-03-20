from django.conf.urls import url

from chemotherapy import views

app_name = 'chemotherapy'

urlpatterns = [
    url(r'^Treatment_plan/ChemoTherapy/Palliative/new/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/$',
        views.new_palliative, name='new_palliative'),
    url(r'^Treatment_plan/ChemoTherapy/Palliative/edit/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/$',
        views.edit_palliative, name='edit_palliative'),

    url(r'^Treatment_plan/ChemoTherapy/NACT/new/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/$',
        views.new_nact, name='new_nact'),
    url(r'^Treatment_plan/ChemoTherapy/NACT/edit/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/$',
        views.edit_nact, name='edit_nact'),

    url(r'^Treatment_plan/ChemoTherapy/ACT/new/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/$',
        views.new_act, name='new_act'),
    url(r'^Treatment_plan/ChemoTherapy/ACT/edit/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/$',
        views.edit_act, name='edit_act'),

    url(r'^Treatment_plan/ChemoTherapy/Concurrent/new/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/$',
        views.new_concurrent, name='new_concurrent'),
    url(r'^Treatment_plan/ChemoTherapy/Concurrent/edit/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/$',
        views.edit_concurrent, name='edit_concurrent'),

]
