from django.db import models

# Create your models here.
class Peripheral(models.Model):
    display_name = models.CharField(max_length=30)
    pin_number = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.display_name

class SubordinatePi(models.Model):
    display_name = models.CharField(max_length=50)
    ip_address = models.GenericIPAddressField()
    port = models.PositiveIntegerField(default=8080)

    def __str__(self):
        return self.display_name
