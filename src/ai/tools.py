
from documents.models import Document
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool

@tool
def documents_list(config:RunnableConfig):
    """ get all documents for this user """
    meta_data = config.get('user_id') or config.get('configurable')
    user_id = meta_data.get('user_id')
    doc_objs = Document.objects.filter(owner_id =user_id,active=True)
    response_data = []
    for doc in doc_objs:
        response_data.append(
            {
                'id':doc.id,
                'title' : doc.title   
            }
        )
        
    return response_data
@tool
def get_document(document_id:int,config:RunnableConfig):
    """ get a document with document id for the this user """
    meta_data = config.get('user_id') or config.get('configurable')
    user_id = meta_data.get('user_id')
    doc_obj = Document.objects.get(pk=document_id,owner_id=user_id)
    
    response_data = {
        'id':doc_obj.id,
        'title':doc_obj.title
    }
    return response_data
    