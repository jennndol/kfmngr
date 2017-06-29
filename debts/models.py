from django.db import models
from suppliers.models import Supplier

class Debt(models.Model):
    """docstring for Loan."""
    supplier = models.ForeignKey(Supplier)
    debt_nominal = models.IntegerField()

    def __init__(self, arg):
        super(Loan, self).__init__()
        self.arg = arg
