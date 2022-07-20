from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('auth:profile', args=(self.pk,))
