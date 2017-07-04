from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^login/$', auth_views.login, {'template_name': 'account/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/account/login'}, name='logout'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^new/$', views.ProfileCreate.as_view(), name='profile-create')
]