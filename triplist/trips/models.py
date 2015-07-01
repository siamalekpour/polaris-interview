import datetime
import os
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

# What this project is
# -------------------
# Instead of creating an app where visitors could view different travel plans,
# I've a created a website where travelers can view trips they've already attended,
# create journals on places they visited, and upload images to each. After signing up of course.
# This is a test so I thought their wouldn't be any harm in changing the objective a bit.


class Profile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profiles')

    def __unicode__(self):
        return '{0} {1}'.format(self.user.first_name, self.user.first_name).strip()

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')


class Continent(models.Model):
    name = models.CharField(_('Name'), max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Continent')
        verbose_name_plural = _('Continents')


class Country(models.Model):
    continent = models.ForeignKey(Continent)
    name = models.CharField(_('Name'), max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')


class TripType(models.Model):
    """
    Could've been a ChoiceField, just figured the updates would be a lot
    For now its, Yolo, Comfort, Active, ....
    """
    name = models.CharField(_('Name'), max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Trip Type')
        verbose_name_plural = _('Trip Types')


class Trip(models.Model):
    type = models.ForeignKey(TripType)
    country = models.ForeignKey(Country)
    name = models.CharField(_('Name'), max_length=200)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('trip-detail', args=(self.id,))

    class Meta:
        verbose_name = _('Trip')
        verbose_name_plural = _('Trips')


class Traveler(models.Model):
    """
    People participating in a trip together
    Each traveler can have a memoir - called a journal
    """
    user = models.ForeignKey(User)
    trip = models.ForeignKey(Trip)
    journal = models.TextField(_('Journal'), blank=True, null=True)

    def __unicode__(self):
        return '{0} {1}'.format(self.user.first_name, self.user.first_name).strip()

    class Meta:
        verbose_name = _('Traveler')
        verbose_name_plural = _('Travelers')


class DestinationType(models.Model):
    """ Destinations have types like restaurants, picnic areas, beaches etc."""
    name = models.CharField(_('Name'), max_length=100)
    slug = models.SlugField(_('Unique Identifier'))  # Mainly used as an icon for map markers

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _('Destination Type')
        verbose_name_plural = _('Destination Types')


class Destination(models.Model):
    """ Travelers can visit many places during their trip """
    trip = models.ForeignKey(Trip)
    type = models.ForeignKey(DestinationType)
    name = models.CharField(_('Name'), max_length=200)
    latitude = models.CharField(_('Lattitude'), max_length=20)
    longitude = models.CharField(_('Longitude'), max_length=20)
    # latitude and longitudes could have also been decimal,
    # but since I'm going to be using Google maps it won't differ
    date = models.DateTimeField(_('Date & Time'), default=datetime.datetime.now)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['date']
        verbose_name = _('Destination')
        verbose_name_plural = _('Destinations')


class Media(models.Model):

    EXTENSIONS = (
        ('image', ('.jpg', '.gif', '.png', '.bmp', '.jpeg')),
        ('video', ('.avi', '.wmv', '.mpeg')),
        'unknown'
    )

    destination = models.ForeignKey(Destination)
    file = models.FileField()
    type = models.CharField(_('File type'), max_length=10)

    def save(self, *args, **kwargs):
        self.type = self.get_type()
        super(Media, self).save(*args, **kwargs)

    def get_type(self):
        type = 'unknown'
        (dir, file) = os.path.split(str(self.file))
        (file_name, extension)=os.path.splitext(file)
        extension = extension.lower()
        for type in self.EXTENSIONS:
            if extension in type[1]:
                type = type[0]
                break
        return type

    def __unicode__(self):
        return self.file.name

    class Meta:
        verbose_name = _('Media')
        verbose_name_plural = _('Media')


class MediaComment(models.Model):
    media = models.ForeignKey(Media)
    user = models.ForeignKey(User)
    comment = models.TextField()
