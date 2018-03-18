from django.conf.urls import url

from followup import views

app_name = 'followup'


urlpatterns = [
    url(r'^(?P<p_id>[0-9]+)/edit_followup/(?P<si_no>[0-9]+)$', views.edit_followup, name='edit_followup'),
    url(r'^(?P<p_id>[0-9]+)/new_followup/$', views.new_followup, name='new_followup'),

]
