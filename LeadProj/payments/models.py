from django.db import models
from django.conf import settings

class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=(
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    ))
    created_at = models.DateTimeField(auto_now_add=True)