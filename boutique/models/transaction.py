from django.db import models

class Transaction(models.Model):
    order = models.OneToOneField("Order", on_delete=models.DO_NOTHING, related_name="transaction")

    date = models.DateTimeField(auto_now_add=True, null=True)