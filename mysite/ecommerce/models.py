from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Ticket(models.Model):
    name=models.CharField(max_length=100)
    start_date=models.DateTimeField(verbose_name=_("start_date"))
    end_date=models.DateTimeField(verbose_name=_("end_date"))
    code=models.IntegerField(unique=True)

class Order(models.Model):
    create_date=models.DateTimeField()
    price=models.CharField(max_length=10)
    ticket=models.ForeignKey(Ticket, on_delete=models.CASCADE)