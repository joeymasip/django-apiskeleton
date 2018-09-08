from django.conf.urls import url
from apiapp.views import user


urlpatterns = [
    url(r'^user/$', user.api_admin_user_index, name='api_admin_user_index'),
    url(r'^user/(?P<pk>[0-9]+)/$', user.api_admin_user_detail, name='api_admin_user_detail'),
]