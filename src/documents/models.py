from django.db import models
from config.settings import AUTH_USER_MODEL

user = AUTH_USER_MODEL
# Create your models here.
class Documents(models.Model):
    owner = models.ForeignKey(user,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)