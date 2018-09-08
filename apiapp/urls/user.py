from django.conf.urls import url
from apiapp.views import user


urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', user.api_user_detail, name='api_user_detail'),
]