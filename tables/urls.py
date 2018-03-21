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
    # ---------------------------------------------------------------------------------------
    url(r'^edit_cobaltcycle/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/(?P<sino>[0-9]+)$',
            views.edit_cobaltcycle, name='edit_cobaltcycle'),
    url(r'^new_cobaltcycle/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/$', views.new_cobaltcycle, name='new_cobaltcycle'),

    url(r'^edit_linaccycle/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/(?P<sino>[0-9]+)$',
            views.edit_linaccycle, name='edit_linaccycle'),
    url(r'^new_linaccycle/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/$', views.new_linaccycle, name='new_linaccycle'),

url(r'^edit_brachycycle/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/(?P<sino>[0-9]+)$',
            views.edit_brachycycle, name='edit_brachycycle'),
    url(r'^new_brachycycle/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/$', views.new_brachycycle, name='new_brachycycle'),

]
