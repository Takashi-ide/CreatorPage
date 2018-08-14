from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout,{'next_page': 'login'}, name='logout'),
    url(r'^admin/', admin.site.urls),
]
