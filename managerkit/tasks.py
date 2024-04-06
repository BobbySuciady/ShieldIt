

# In your tasks.py
from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import Item, ExpiringItem

@shared_task
def check_expiry_dates():
    one_week_ahead = timezone.now().date() + timedelta(days=7)
    expiring_items = Item.objects.filter(expiry_date__lte=one_week_ahead, expiry_date__gte=timezone.now().date())
    for item in expiring_items:
        # Create or update ExpiringItem entry
        ExpiringItem.objects.update_or_create(
            name=item.name,
            expiry_date=item.expiry_date
        )