from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'account/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'account/login.html'}, name='logout'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile')
]