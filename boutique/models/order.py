from django.db import models
from datetime import datetime 

from .ordered_product import OrderedProduct

class Order(models.Model):
    class Status(models.Choices):
        ATTENTE="en_attente"
        LIVRAISON="en_livraison"
        ANNULER="annuler"

    client = models.ForeignKey("auth.User", on_delete=models.DO_NOTHING, related_name="orders")
    status = models.CharField(choices=Status.choices, max_length=20, default=Status.ATTENTE, null=False)

    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    def add_product(self, product, quantity):
        OrderedProduct.objects.create(product=product, quantity=quantity, order=self)
        