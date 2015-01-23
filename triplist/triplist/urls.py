from django.conf.urls import patterns, include, url
from django.contrib import admin
from trips.views import TripView

urlpatterns = patterns('',
    url(r'^$', TripView.as_view()),
    url(r'^api/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
