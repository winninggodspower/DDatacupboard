from django.db import models
from django.core.mail import send_mail
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
import threading

# Create your models here.
class Data(models.Model):
    preview_image = models.ImageField(upload_to='data_images')
    title         = models.CharField(max_length=50)
    description   = models.TextField()
    data_file     = models.FileField(upload_to='data-file')

    def __str__(self):
        return self.title
    
class Feedback(models.Model):
    WOULD_RECOMMEND_CHOICES = [
        ('yes', 'yes'),
        ('no', 'no'),
        ('maybe', 'maybe'),
    ]
    name    = models.CharField(max_length=50)
    email   = models.EmailField(max_length=254)
    service_rating = models.PositiveIntegerField()
    would_recommend = models.CharField(max_length=50, choices=WOULD_RECOMMEND_CHOICES)
    additional_feedback = models.TextField()



@receiver(post_save, sender=Feedback)
def send_feedback_email(sender, instance, created, **kwargs):

    if created:
        subject = 'New Datacupboard Feedback'
        message = f'''
        NAME:            {instance.name}
        EMAIL:           {instance.email}
        service_rating:  {instance.service_rating}/5
        would_recommend: {instance.would_recommend}

        additional_feedback:
        {instance.additional_feedback}
        '''
        
        thread = threading.Thread(target=lambda: send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['destrorobotics@gmail.com'],
        ))
        thread.start()