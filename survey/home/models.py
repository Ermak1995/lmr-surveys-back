from django.db import models
import uuid
class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Surveys(models.Model):
    uuid = models.UUIDField(unique=True, default=None)
    access_hash = models.UUIDField(unique=True, default=None)
    survey = models.JSONField()
