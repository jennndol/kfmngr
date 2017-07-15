from django.db import models

class History(models.Model):
    """docstring for History."""
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated_at = models.DateTimeField(auto_now_add = False, auto_now = True)

    class Meta:
        verbose_name_plural = 'Histories'

    def __str__(self):
        return self.text

    @classmethod
    def create(cls, text):
        history = cls(text=text)
        return history
