
from documents.models import UserPersonalInfo
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool
from django.db.models import Q

def save_personal_info(info_title:str,info:str,config:RunnableConfig):
    """
    use this tool to save user personal info like Name,Number,City,Mood,...etc
    
    args:
    info_title: str 255 char max use somthing that you can understand later like USER_NAME or USER FIRST NAME
    info: content mo limit write something you can understand later
    """
    configurable = config.get('configurable') or config.get('meta_data')
    user_id = configurable.get('user_id')
    if user_id==None:
        raise Exception('invalid request for user')
    
    info_obj = UserPersonalInfo.objects.create(user_id=user_id,info_title=info_title,info=info)
    response_data={
                'id':info_obj.pk,
                'title' : info_obj.info_title,
                'content' : info_obj.info,
                'created_at': info_obj.created_at
                
                }
            
    return response_data


personal_info_tools_list = [save_personal_info]