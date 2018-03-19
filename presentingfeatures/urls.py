from django.conf.urls import url
from django.urls import path, include

from presentingfeatures import views

app_name = 'pf'
urlpatterns = [
    url(r'^(?P<p_id>[0-9]+)/Status/new/$', views.new_status, name='new_status'),
    url(r'^(?P<p_id>[0-9]+)/Status/edit/$', views.edit_status, name='edit_status'),
    #
    url(r'^Investigations/new/(?P<p_id>[0-9]+)/$', views.upload_handler, name='upload_handler'),
    url(r'^Investigations/download/(?P<p_id>[0-9]+)/(?P<ftype>[\w\-]+)/(?P<num>[0-9]+)/$', views.download_file,
        name='download_file'),
    url(r'^Investigations/delete/(?P<p_id>[0-9]+)/(?P<ftype>[\w\-]+)/(?P<num>[0-9]+)/$', views.delete_file,
        name='delete_file'),

]