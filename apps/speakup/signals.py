from django.db.models.signals import post_delete
from django.db.models.signals import post_init
from django.db.models.signals import post_save
from django.dispatch import receiver

from adhocracy4.images import services as image_services

from .models import SpeakupIdea


@receiver(post_init, sender=SpeakupIdea)
def backup_image_path(sender, instance, **kwargs):
    instance._current_image_file = instance.image


@receiver(post_save, sender=SpeakupIdea)
def delete_old_image(sender, instance, **kwargs):
    if hasattr(instance, '_current_image_file'):
        if instance._current_image_file != instance.image:
            image_services.delete_images([instance._current_image_file])


@receiver(post_delete, sender=SpeakupIdea)
def delete_images_for_SpeakupIdea(sender, instance, **kwargs):
    image_services.delete_images([instance.image])
