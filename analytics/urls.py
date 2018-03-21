from django.conf.urls import url

from analytics import views

app_name = 'analytics'

urlpatterns = [
    url(r'^result/form_handle/$', views.form_handle, name='form_handle'),
    url(r'^result/form_handle_pk/$', views.form_handle_pk, name='form_handle_pk'),
]
