from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import CustomUser
from mypermit import permit
from asgiref.sync import async_to_sync
from permit import RoleAssignmentCreate

   
@receiver(signal=post_save,sender=CustomUser)
def sync_created_user_with_permit(sender,instance,created,**kwargs):
    if created:
        user_data = {
            "key":f"{instance.id}",
        }
        if instance.first_name:
            user_data['first_name'] = f"{instance.first_name}"
        else:
            user_data['first_name'] = f"{instance.username}"
        if instance.last_name:
            user_data['last_name'] = f"{instance.last_name}"
        if instance.email:
            user_data['email'] = f"{instance.email}"
            
        async_to_sync(permit.api.users.sync)(user_data)
    
        assingment =RoleAssignmentCreate(user=f"{instance.id}",role="viewer",tenant="default")
        
        async_to_sync(permit.api.users.assign_role)(assingment)                                                        