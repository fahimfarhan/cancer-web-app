from django.conf.urls import url

from referralnote import views

app_name = 'referral_note'

#view_obj = views.ReferralNotes()

urlpatterns = [
    url(r'^(?P<p_id>[0-9]+)/delete_referralnote/(?P<notenum>[0-9]+)$', views.delete_refnote,
        name='delete_referralnote'),
    url(r'^(?P<p_id>[0-9]+)/edit_referralnote/(?P<notenum>[0-9]+)$', views.edit_referralnote, name='edit_referralnote'),
    url(r'^(?P<p_id>[0-9]+)/new_referralnote/$', views.new_referralnote, name='new_referralnote'),

]
