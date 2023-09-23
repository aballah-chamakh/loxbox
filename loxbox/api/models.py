from django.db import models
from django.contrib.auth.models import User  # Import the default User model

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Transaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
