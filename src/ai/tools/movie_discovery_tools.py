from urllib import response
from langchain_core.runnables import RunnableConfig
from tmdb.client import search_movie as tmdb_search_movie,movie_detail as tmdb_movie_detail
from mypermit import permit
from asgiref.sync import async_to_sync



def search_movie(query:str,limit=5,config:RunnableConfig={}):
    
    """ search the most recent LIMIT movies from THE MOVIE DATA BASE API with the max of 25
    
    arguments:
    query: an string use this to search for a movie title
    limit: number of results dont bring back more than that
    
    """
    configurable = config.get('configurable') or config.get('metadata')
    user_id = configurable.get('user_id')
    has_perm = async_to_sync(permit.check)(f'{user_id}','search','movie_disovery')
    if not has_perm:
        raise Exception('you do not have permission to search movie information')
    
    print('Searching with user', user_id)
    
    response = tmdb_search_movie(query=query)
        
    try:
        total_results = int(response.get('total_results'))
    except:
        total_results = -1
        
    if total_results==0:
        return[]
    
    if limit>25:
        limit=25
        
    return response.get('results')[:limit]

def movie_detail(movie_id:int,config:RunnableConfig={}):
    """ get a movie detail using (movie_id) from The movie database
    
    arguments:
    movie_id : get it from search_movie the movie database return movie_id to lookup movie detail when using search api
    
    """
    configurable = config.get('configurable') or config.get('metadata')
    user_id = configurable.get('user_id')
    has_perm = async_to_sync(permit.check)(f'{user_id}','detail','movie_disovery')
    if not has_perm:
        raise Exception('you do not have permission to get moive detail')
    print('Searching with user', user_id)
    
    response = tmdb_movie_detail(movie_id=movie_id)
    
    return response


movie_discovery_tools_list = [movie_detail,search_movie]
