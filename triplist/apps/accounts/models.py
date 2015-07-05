from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

class Profile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profiles')

    def __unicode__(self):
        return '{0} {1}'.format(self.user.first_name, self.user.last_name).strip()

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')


@receiver(post_save, sender=User)
def user_handler(sender, instance, created, **kwargs):
    if created:
        Profile(user=instance).save()
