import uuid
from django.db.models.signals import pre_save
from django.dispatch import receiver

from cars.models import Car


@receiver(pre_save, sender=Car)
def pre_save_create_code(sender, instance, **kwargs):
    if instance.code == '':
        instance.code = str(uuid.uuid4()).replace('-', '')[:10]
