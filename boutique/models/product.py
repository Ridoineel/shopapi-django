from django.db import models, transaction

class Product(models.Model):
    class Currency(models.Choices):
        F_CFA="XOF"
        EURO="EUR"

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    currency = models.CharField(choices=Currency.choices, max_length=10, default=Currency.F_CFA)
    active = models.BooleanField(default=True)

    image = models.ImageField(upload_to="", blank=True, null=True) # upload_to="static/product/images"
    image_url = models.URLField(null=True)
    
    category = models.ForeignKey('boutique.Category', on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
