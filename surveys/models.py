
from django.db import models

class Survey(models.Model):
    """A Survey represents a Survey
    """
    name        = models.CharField(max_length=12)
    description = models.CharField(max_length=64)
    link        = models.CharField(max_length=64)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return '<a href="%s">%s</a>' % (self.link, self.description)

