from django.db import models
from buyings.models import Buying

class Paying(models.Model):
    """docstring for Paying."""
    buying = models.ForeignKey(Buying)
    paying_nominal = models.IntegerField()

    def __init__(self, arg):
        super(Paying, self).__init__()
        self.arg = arg
