from django.db import models

class School(models.Model):

    name = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    province = models.CharField(max_length=64)
    zip = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    website = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    email = models.EmailField()
    vat = models.CharField(max_length=64)

    def __str__(self):
        return self.name