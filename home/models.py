from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name