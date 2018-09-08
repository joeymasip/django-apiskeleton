from django.conf.urls import url, include


urlpatterns = [
    url(r'^admin/', include('apiapp.urls.admin')),
    url(r'^auth/', include('apiapp.urls.registration')),
    url(r'^user/', include('apiapp.urls.user')),
]