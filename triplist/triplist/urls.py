from django.conf.urls import patterns, include, url
from django.contrib import admin
from trips import views as trip_views


urlpatterns = patterns('',
    url(r'^$',                 trip_views.TripListView.as_view(),   name='trip-list'),
    url(r'^(?P<pk>\d+)/$',     trip_views.TripDetailView.as_view(), name='trip-detail'),
    url(r'^api/$',             trip_views.TripApiList.as_view()),
    url(r'^api/(?P<pk>\d+)/$', trip_views.TripApiDetail.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
