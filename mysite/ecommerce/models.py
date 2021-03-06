from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()





class Ticket(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField(verbose_name=_("start_date"))
    end_date = models.DateTimeField(verbose_name=_("end_date"))
    code = models.IntegerField(unique=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    price = models.CharField(max_length=10)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    def __str__(self):
        return self.ticket.name

    

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user.balance =int(self.user.balance)-int(self.price)
            self.user.save()
        super(Order,self).save(*args,**kwargs)
