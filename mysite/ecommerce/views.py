from django.core import paginator
from django.shortcuts import render, HttpResponse,redirect
from django.contrib import auth
from django.conf import settings
from django.contrib.auth import logout
from .models import Ticket,Order
import datetime
from django.db.models import Sum, Q, Count
from django.utils import timezone
from .forms import OrderForm
from django.contrib.auth import get_user_model
User = get_user_model()
from .forms import OrderForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



app_name = 'ecommerce'

def order_list(request):
    order_list = Order.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(order_list,3)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    ticket = request.POST.get('ticket')
    ticket_search = Order.objects.filter(ticket__name=ticket).all()
    return render(request, 'ecommerce/tickets.html', {'users':users, 'ticket':ticket_search})

def logout(request):
    auth.logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)

def home(request):
    today = datetime.datetime.now()
    user_statistic = Order.objects.filter(user_id=request.user.id)\
    .aggregate(in_year=Count('create_date',filter=Q(create_date__gte=today-timezone.timedelta(days=365))),
    in_month=Count('create_date',filter=Q(create_date__gte=today-timezone.timedelta(weeks=4))),
    in_week=Count('create_date',filter=Q(create_date__gte=today-timezone.timedelta(days=7))),
    sum_in_week=Sum('price',filter=Q(create_date__gte=today-timezone.timedelta(days=7))),
    sum_in_month=Sum('price',filter=Q(create_date__gte=today-timezone.timedelta(weeks=4))),
    sum_in_year=Sum('price',filter=Q(create_date__gte=today-timezone.timedelta(days=365))))


    form = OrderForm(request=request)
    if request.method=="POST":
        form=OrderForm(data=request.POST,request=request)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
    
    return render(request, 'ecommerce/home.html', {'stat':user_statistic, 'form':form})



