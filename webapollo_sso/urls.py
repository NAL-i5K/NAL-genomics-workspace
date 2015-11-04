from django.conf.urls import patterns, url, include
from . import views

urlpatterns = patterns('',
    url(r'^$', views.create, name='create'),
    url(r'^get_users$', views.get_users, name='get_users'),
    url(r'^get_groups$', views.get_groups, name='get_groups'),
    url(r'^get_my_organism$', views.get_my_organism, name='get_my_organism'),
    url(r'^get_my_request$', views.get_my_request, name='get_my_request'),
    url(r'^get_pending_request$', views.get_pending_request, name='get_pending_request'),
    url(r'^make_request$', views.make_request, name='make_request'),
    url(r'^handle_request$', views.handle_request, name='handle_request'),
    url(r'^create_user$', views.create_user, name='create_user'),
    url(r'^delete_user$', views.delete_user, name='delete_user'),
    url(r'^update_user$', views.update_user, name='update_user'),
    url(r'^disconnect_user$', views.disconnect_user, name='disconnect_user'),
    url(r'^check_django_user_available$', views.check_django_user_available, name='check_django_user_available'),
    url(r'^add_user_to_group$', views.add_user_to_group, name='add_user_to_group'),
    url(r'^remove_user_from_group$', views.remove_user_from_group, name='remove_user_from_group'),
    url(r'^create_group_for_organism$', views.create_group_for_organism, name='create_group_for_organism'),
    url(r'^delete_group_for_organism$', views.delete_group_for_organism, name='delete_group_for_organism'),
    url(r'^get_all_groups$', views.get_all_groups, name='get_all_groups'),
    url(r'^check_organism_exist$', views.check_organism_exist, name='check_organism_exist'),
)
