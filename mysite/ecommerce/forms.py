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

    def __init__(self,request,*args,**kwargs):
        super(OrderForm,self).__init__(*args,**kwargs)
        self.request=request

    class Meta:
        model = Order
        fields=("price", "ticket")

    def clean_price(self):
        price = self.cleaned_data['price']
        user_balance=self.request.user.balance
        if int(price)>user_balance:
            raise forms.ValidationError("თანხა არ არის ")
        return price

    