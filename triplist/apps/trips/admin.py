from django.contrib import admin

from apps.trips.models import Continent, Country, TripType, Trip, Traveler, DestinationType, Destination, Media, MediaComment


class DestinationInline(admin.TabularInline):
    model = Destination
    extra = 0

class TravelerInline(admin.TabularInline):
    model = Traveler
    extra = 0
    fields = ('user',)

class CommentInline(admin.TabularInline):
    model = MediaComment
    extra = 0

class TripAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'country',)
    list_filter = ('type', 'country',)
    inlines = [DestinationInline, TravelerInline]


class MediaAdmin(admin.ModelAdmin):
    list_display = ('file', 'type', 'destination', )
    list_filter = ('type',)
    inlines = [CommentInline,]

admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(TripType)
admin.site.register(Trip, TripAdmin)
admin.site.register(DestinationType)
admin.site.register(Media, MediaAdmin)
