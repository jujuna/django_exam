from ecommerce.models import Ticket, Order
from django import forms


TicketForm(forms.ModelForm):
    class Meta:
        model=Ticket

OrderForm(forms.ModelForm):
    class Meta:
        model=Order