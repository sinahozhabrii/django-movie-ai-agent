from typing import Iterable
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.
USER = get_user_model()
class Document(models.Model):
    owner = models.ForeignKey(USER,on_delete=models.CASCADE)
    title = models.CharField(max_length=255,default='Title')
    content = models.TextField(blank=True,null=True)
    active = models.BooleanField(default=True)
    active_at  = models.DateTimeField(auto_now=False,auto_now_add=False,default=None,null=True,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.title}'
    
    
    def save(self,*args, **kwargs):
        if self.active and self.active_at == None:
            self.active_at = timezone.now()
        else:
            self.active_at = None
            
        return super().save(*args,**kwargs)