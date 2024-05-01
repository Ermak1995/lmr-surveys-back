from django.db import models
import uuid


class Surveys(models.Model):
    uuid = models.UUIDField(unique=True, default=None)
    access_hash = models.UUIDField(unique=True, default=None)
    survey = models.JSONField()
