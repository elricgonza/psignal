from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from polls.models import Question, Choice
import os.path


@receiver(post_save, sender=Question)
@receiver(post_save, sender=Choice)
def model_post_save(sender, **kwargs):
    print('Grabadex: {}'.format(kwargs['instance'].__dict__))
    print('********************')




