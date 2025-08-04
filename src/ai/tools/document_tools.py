
from documents.models import Document
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool
from django.db.models import Q
from mypermit import permit as permit_client
from asgiref.sync import async_to_sync

permit = permit_client

@tool
def search_query_documents(query:str,config:RunnableConfig= {}):
    """ search documents using arguments

        argument:
        
        query: you can use it to search to find documents that their title or content contains this argument
    
    """

    configurable = config.get('configurable') or config.get('meta_data')
    user_id = configurable.get('user_id')
    defualt_look_up = {
        'active' : True,
        'owner_id' : user_id
    }
    has_perm = async_to_sync(permit.check)(f'{user_id}','read','document')
    if not has_perm:
        raise Exception('you do not have permission to read document')
    try:
        doc_objs = Document.objects.filter(**defualt_look_up).filter(Q(title__icontains=query)|Q(content__icontains=query))
    except Document.DoesNotExist:
        raise Exception('Document not found or you do not have access to it try again')
    except:
        raise Exception('Something went wrong while fetching the documents invalid request')
    response_data = []
    for doc in doc_objs:
        response_data.append(
            {
                'id':doc.id,
                'title' : doc.title,
                'content':doc.content, 
                  
            }
        )
        
    return response_data
        
@tool
def documents_list(config:RunnableConfig= {}):
    """ list 5 recent documents for this user """
    configurable = config.get('configurable') or config.get('meta_data')
    user_id = configurable.get('user_id')
    has_perm = async_to_sync(permit.check)(f'{user_id}','read','document')
    if not has_perm:
        raise Exception('you do not have permission to read document')
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
                'id':doc.id,
                'title' : doc.title   
            }
        )
    
        
    return response_data
@tool
def get_document(document_id:int,config:RunnableConfig={}):
    """ get a document with document id for the this user """
    configurable = config.get('configurable') or  config.get('meta_data') 
    user_id = configurable.get('user_id')
    has_perm = async_to_sync(permit.check)(f'{user_id}','read','document')
    if not has_perm:
        raise Exception('you do not have permission to read document')
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


@tool
def create_documents(title:str,content:str,config:RunnableConfig= {}):
    """ 
    create a new document in database with given arguments
    
    title: max 120 charcter
    content = without limit long form text in many paragraphs or pages 
    
    """
    

    configurable = config.get('configurable') or config.get('meta_data')
    user_id = configurable.get('user_id')
    if user_id == None:
        raise Exception('invalid request for user')
    
    has_perm = async_to_sync(permit.check)(f'{user_id}','create','document')
    if not has_perm:
        raise Exception('you do not have permission to create document')

        
    doc_obj = Document.objects.create(owner_id = user_id,title=title,content=content,active=True)
    
    response_data={
                'id':doc_obj.id,
                'title' : doc_obj.title,
                'content' : doc_obj.content,
                'created_at': doc_obj.create_at
                
                }
            
    return response_data


@tool
def delete_documents(document_id:int,config:RunnableConfig= {}):
    """ 
    delete a document for this user
    
    be careful when using this tool only use it when user ask for it clearly!!!!
    
    """

    configurable = config.get('configurable') or config.get('meta_data')
    user_id = configurable.get('user_id')
    if user_id == None:
        raise Exception('invalid request for user')
    has_perm = async_to_sync(permit.check)(f'{user_id}','delete','document')
    if not has_perm:
        raise Exception('you do not have permission to delete document')
    try:
        doc_obj = Document.objects.get(owner_id = user_id,pk=document_id,active=True)
    except Document.DoesNotExist:
        raise Exception('document not found, try again!')
    except:
        raise Exception('invalid request for getting document detail, try again!')
    doc_obj.delete()
    response_data={'message':'Success'}
            
    return response_data

@tool
def update_documents(document_id:int,title:str =None,content:str =None,config:RunnableConfig= {}):
    """ 
    update  a document for this user
    
    arguments are:
    
    document_id : id or pk of document(required)
    title: string max lenght 120 char(optional)
    content : without limit long form text in many paragraphs or pages  (optional)
    """

    configurable = config.get('configurable') or config.get('meta_data')
    user_id = configurable.get('user_id')
    if user_id == None:
        raise Exception('invalid request for user')
    has_perm = async_to_sync(permit.check)(f'{user_id}','update','document')
    if not has_perm:
        raise Exception('you do not have permission to update document')
    try:
        doc_obj = Document.objects.get(owner_id = user_id,pk=document_id,active=True)
    except Document.DoesNotExist:
        raise Exception('document not found, try again!')
    except:
        raise Exception('invalid request for getting document detail, try again!')
    if title is not None:
        doc_obj.title = title
    if content is not None:
        doc_obj.content = content
    if content or title:
        doc_obj.save()
        response_data =  {
        "id": doc_obj.id,
        "title": doc_obj.title,
        "content": doc_obj.content,
        "created_at": doc_obj.create_at
    }
            
    return response_data




document_tools_list = [documents_list,get_document,create_documents,delete_documents,update_documents,search_query_documents]