from django.db import models
from django.contrib.auth.models import User

class Tematy(models.Model):
    """Kategorie tematyczne blogów"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='blog_owner')

    def __str__(self):
        return self.text

class Wpisy(models.Model):
    temat = models.ForeignKey(Tematy, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'wpisy'

    def __str__(self):
        return f"{self.text[:50]}..."