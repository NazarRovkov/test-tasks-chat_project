from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class ThreadManager(models.Manager):
    def get_last_messages(self):
        return self.annotate(last_message=Max('messages__created')).order_by('-last_message')

class Thread(models.Model):
    participants = models.ManyToManyField(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = ThreadManager()

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
