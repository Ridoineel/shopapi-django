from django.db import models

def timestanp(cls):
    cls.date_created = models.DateTimeField(auto_now_add=True)
    cls.date_updated = models.DateTimeField(auto_now=True)

    return cls