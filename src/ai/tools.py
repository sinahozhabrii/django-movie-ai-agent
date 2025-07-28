
from documents.models import Document
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool

@tool
def documents_list(config:RunnableConfig= {}):
    """ list 5 recent documents for this user """
    print(config)
    configurable = config.get('configurable') or config.get('meta_data')
    user_id = configurable.get('user_id')
    try:
        doc_objs = Document.objects.filter(owner_id =user_id,active=True).order_by('-create_at')[:5]
    except Document.DoesNotExist:
        raise Exception('Document not found or you do not have access to it try again')
    except:
        raise Exception('Something went wrong while fetching the documents invalid request')
    response_data = []
    for doc in doc_objs:
        response_data.append(
            {
                'id':doc.pk,
                'title' : doc.title   
            }
        )
        
    return response_data
@tool
def get_document(document_id:int,config:RunnableConfig={}):
    """ get a document with document id for the this user """
    configurable = config.get('configurable') or  config.get('meta_data') 
    user_id = configurable.get('user_id')
    try:
        doc_obj = Document.objects.get(pk=document_id,owner_id=user_id)
    except Document.DoesNotExist:
        raise Exception('Document not found or you do not have access to it try again')
    except:
        raise Exception('Something went wrong while fetching the document invalid request')
    response_data = {
        'id':doc_obj.id,
        'title':doc_obj.title
    }
    return response_data


tools_list = [documents_list,get_document]