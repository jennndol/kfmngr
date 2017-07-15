from django.db import models

class History(models.Model):
    """docstring for History."""
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated_at = models.DateTimeField(auto_now_add = False, auto_now = True)

    def __str__(request):
        return self.text
