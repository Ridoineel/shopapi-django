from django.db import models

class OrderedProduct(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    order = models.ForeignKey("Order", on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        return f"{self.product}: {self.quantity}"