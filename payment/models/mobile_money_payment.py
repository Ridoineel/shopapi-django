from django.db import models
from .payment import Payment

class MobileMoneyPayment(Payment):
    class Operators(models.Choices):
        TMONEY="T-MONEY"
        FLOOZ="FLOOZ"

    phoneNumber = models.CharField(max_length=30)
    operator = models.CharField(choices=Operators.choices, max_length=20)
    payment_reference = models.CharField(max_length=100, unique=True)