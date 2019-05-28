from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^example/$', views.example, name='a_fake_plugin-example_view'),
    url(r'^fail-testcases-report/$', views.get, name='telemetry-testruns-get'),
]

