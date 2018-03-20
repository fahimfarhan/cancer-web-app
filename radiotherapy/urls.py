from django.conf.urls import url

from radiotherapy import views

app_name = 'radiotherapy'



urlpatterns = [
    url(r'^Treatment_plan/RadioTherapy/Cobalt/new/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/$', views.new_Cobalt, name='new_Cobalt'),
]
