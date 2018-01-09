from django.conf.urls import url
from .views import *

app_name = 'df_user'
urlpatterns = [
    url(r'^user/register$', register, name='register'),
    url(r'^user/register_handle$', register_handle, name='register_handle'),
    url(r'^user/login$', login, name='login'),
    url(r'^user/register_exist', register_exist, name='register_exist'),
    url(r'^user/find_password$', find_password, name='find_password'),
    url(r'^user/login_handle$', login_handle, name='login_handle'),
    url(r'^user/user_exist', user_exit, name='user_exit'),
]