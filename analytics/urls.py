from django.conf.urls import url

from analytics import views

app_name = 'analytics'

urlpatterns = [
    url(r'^result/form_handle/$', views.form_handle, name='form_handle'),
    url(r'^result/form_handle_pk/$', views.form_handle_pk, name='form_handle_pk'),
    url(r'^result/stage_one_query/$', views.stage_one, name='sq_stage_one'),
    url(r'^result/stage_two_query/$', views.stage_two, name='sq_stage_two'),
    url(r'^result/stage_three_query/$', views.stage_three, name='sq_stage_three'),
    url(r'^result/stage_four_query/$', views.stage_four, name='sq_stage_four'),
    url(r'^result/linac/$',views.linac,name='sq_linac'),
    url(r'^result/cobalt/$',views.cobalt,name='sq_cobalt'),
    url(r'^result/brachy/$',views.brachy,name='sq_brachy'),
    url(r'^result/nact/$', views.nact, name='sq_nact'),
    url(r'^result/act/$', views.act, name='sq_act'),
    url(r'^result/concurrent/$', views.concurrent, name='sq_concurrent'),
    url(r'^result/palliative/$', views.palliative, name='sq_palliative'),

]
