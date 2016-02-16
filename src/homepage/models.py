from __future__ import unicode_literals

from django.db import models

# Create your models here.

class blog(models.Model):
    title = models.CharField(max_length = 100)
    context = models.TextField()
    after= models.DateTimeField()
    initial = models.DateTimeField()
    checklist = models.BinaryField(default = 'False')

    def __unicode__(self):
        return self.title



