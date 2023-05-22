from django.db import models
from .payment import Payment
from django.core.validators import MaxLengthValidator

class CreditCardPayment(Payment):
    card_number = models.IntegerField(validators=[MaxLengthValidator(16)])
    expiration_date = models.DateField()
    cvc = models.IntegerField(validators=[MaxLengthValidator(3)])