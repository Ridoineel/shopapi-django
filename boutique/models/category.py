from django.db import models, transaction

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
