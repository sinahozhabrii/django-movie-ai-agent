from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(("email address"), blank=True,unique=True)
    thread_id = models.UUIDField(default=uuid.uuid4)