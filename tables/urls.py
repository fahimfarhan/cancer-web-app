from django.conf.urls import url

from tables import views

app_name = 'table'

urlpatterns = [
    url(r'^edit_nactcycle/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/(?P<cycleno>[0-9]+)$',
        views.edit_nactcycle, name='edit_nactcycle'),
    url(r'^new_nactcycle/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/$', views.new_nactcycle, name='new_nactcycle'),

    url(r'^edit_actcycle/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/(?P<cycleno>[0-9]+)$',
        views.edit_actcycle, name='edit_actcycle'),
    url(r'^new_actcycle/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/$', views.new_actcycle, name='new_actcycle'),

    url(r'^edit_concurrcycle/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/(?P<cycleno>[0-9]+)$',
        views.edit_concurrcycle, name='edit_concurrcycle'),
    url(r'^new_concurrcycle/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/$', views.new_concurrcycle, name='new_concurrcycle'),

    url(r'^edit_palliativecycle/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/(?P<cycleno>[0-9]+)$',
        views.edit_palliativecycle, name='edit_palliativecycle'),
    url(r'^new_palliativecycle/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/$',
        views.new_palliativecycle, name='new_palliativecycle'),

]