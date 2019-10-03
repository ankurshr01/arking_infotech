from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include



urlpatterns = [
    url(r'^$',views.Home, name='home'),
    url(r'^SignUp/$', views.SignUp, name = 'signup'),
    url(r'^Login/$', views.Login, name = 'login'),
    url(r'^Logout/$', views.Logout, name = 'logout'),
    url(r'^ChangePassword/$', views.ChangePassword, name = 'changepassword'),
    url(r'^home/$', views.Home, name = 'Home'),
    url(r'^Logout/home/$', views.Home, name = 'Home'),
  ]
urlpatterns += staticfiles_urlpatterns()
