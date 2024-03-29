from django.db import models


class Contact(models.Model):
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=10)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    jet=models.TextField()
    budget=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.f_name
