from django.db import models
from django.utils import timezone
# Create your models here.
class MailsToSend(models.Model):
    email = models.EmailField(unique=True)
    registered = models.DateTimeField(default=timezone.now)
