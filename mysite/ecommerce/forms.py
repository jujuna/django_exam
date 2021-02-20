from django.http import request
from ecommerce.models import Ticket, Order
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
User = get_user_model()

class TicketForm(forms.ModelForm):
    
    class Meta:
        model = Ticket
        fields='__all__'

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields=("price", "ticket")

    