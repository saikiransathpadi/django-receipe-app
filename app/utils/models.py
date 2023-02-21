from django.db import models
from django.utils import timezone


class TimestampModel(models.Model):
    created_on = models.DateTimeField(default=timezone.localtime)
    updated_on = models.DateTimeField(default=timezone.localtime)

    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
