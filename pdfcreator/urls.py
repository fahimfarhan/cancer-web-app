from django.conf.urls import url

from pdfcreator import views, summary

app_name = 'pdfcreator'

urlpatterns = [
    url(r'^view/prescription/(?P<p_id>[0-9]+)/(?P<number>[0-9]+)/(?P<user_pk>[0-9]+)/$', views.view_prescription, name='view_prescription'),
    url(r'^pdf/prescription/(?P<p_id>[0-9]+)/(?P<number>[0-9]+)/$', views.print_prescription, name='print_prescription'),
    #
    url(r'^view/referralnote/(?P<p_id>[0-9]+)/(?P<number>[0-9]+)/(?P<user_pk>[0-9]+)/$',
        views.view_referralnote, name='view_referralnote'),
    url(r'^pdf/referralnote/(?P<p_id>[0-9]+)/(?P<number>[0-9]+)/$', views.print_referralnote,
        name='print_referralnote'),
    #
    url(r'^view/report/(?P<user_pk>[0-9]+)/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/$', summary.view_report, name='view_report'),
    url(r'^pdf/report/(?P<p_id>[0-9]+)/(?P<tp_num>[0-9]+)/$', summary.print_report, name='print_report'),

]