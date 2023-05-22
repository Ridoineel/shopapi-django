from django.db import models

class Delivery(models.Model):
    class Status(models.Choices):
        ANNULEE="annulee"
        EN_PREPARATION="en_preparation"
        EN_COURS="en_cours"
        TERMINEE="terminee"

    address = models.CharField(max_length=256)
    phoneNumber = models.CharField(max_length=20)
    lat = models.DecimalField(max_digits=10, decimal_places=7)
    lon = models.DecimalField(max_digits=10, decimal_places=7)
    status = models.CharField(choices=Status.choices, max_length=20, default=Status.EN_PREPARATION)

    order = models.ForeignKey("Order", on_delete=models.CASCADE, related_name="delivery")
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Deliveries"

    def __str__(self):
        return self.address