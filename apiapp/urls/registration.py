from django.conf.urls import url
from apiapp.views import registration


urlpatterns = [
    url(r'^login/', registration.api_login, name='api_login'),
]