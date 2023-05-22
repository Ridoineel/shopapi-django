from django.db import models
from testsn.utils.decorators import timestanp

@timestanp
class Payment(models.Model):
    amount = models.PositiveIntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return f"Payment({self.id})"