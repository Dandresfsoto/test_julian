import uuid

from django.db import models
from .data import TRANSACTION_ENTRY_STR, TRANSACTION_OUT_STR


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    id_number = models.CharField(max_length=20)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Account(models.Model):
    number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.client} - {self.number}"

    def new_transaction(self, transaction_type, amount):

        if transaction_type == TRANSACTION_ENTRY_STR:
            self.amount += amount
        elif transaction_type == TRANSACTION_OUT_STR:
            if self.amount < amount:
                raise ValueError("insufficient funds")
            else:
                self.amount -= amount
        else:
            pass

        self.save()
        return 'process'
