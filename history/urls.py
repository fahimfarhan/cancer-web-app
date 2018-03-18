from django.conf.urls import url

from history import views

app_name = 'history_123'

#hc = HistoryController()

urlpatterns = [

    url(r'^(?P<p_id>[0-9]+)/history/new/$', views.new_history, name='new_history'),
    url(r'^(?P<p_id>[0-9]+)/historyedit/$', views.edit_history, name='edit_history'),
    url(r'^deletehfile/(?P<p_id>[0-9]+)/(?P<num>[0-9]+)/$', views.delete_historyfile, name='delete_historyfile'),
    url(r'^downloadfile/(?P<p_id>[0-9]+)/(?P<num>[0-9]+)/$', views.download_file, name='download_file'),
    url(r'^uploadfile/(?P<p_id>[0-9]+)/$', views.upload_handler, name='upload_handler'),

]
