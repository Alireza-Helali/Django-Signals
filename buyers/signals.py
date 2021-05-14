from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Buyer

user = get_user_model()


@receiver(post_save, sender=user)
def post_save_create_buyer(sender, instance, created, **kwargs):
    print(f'sender : {sender}')
    print(f'instance : {instance}')
    print(f'created : {created}')
    if created:
        Buyer.objects.create(user=instance)
