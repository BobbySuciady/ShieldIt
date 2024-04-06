from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import User, Category, Item

# Ideally we check every time the app opens or a new item / new user (any action is done on the app)
@shared_task
def check_expiry_dates():
    one_week_ahead = timezone.now().date() + timedelta(days=7)
    expiring_items = Item.objects.filter(expiry_date__lte=one_week_ahead, expiry_date__gte=timezone.now().date())
    for item in expiring_items:
        # notification/flagging logic here
        print(f"\n\nItem {item.name} is expiring soon.\n\n")
