import requests
from decouple import config
TMBD_API = config('TMDB_API',default='')


def get_headers():
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMBD_API}" 
    }
    
    return headers

def search_movie(query:str,page:int=1,raw=False):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        'query':query,
        'include_adult':False,
        'page':page,
        'language': 'en-US',     
    }
    
    headers = get_headers()
    
    response = requests.get(url, headers=headers,params=params)

    if raw:
        return response
    
    return response.json()

def movie_detail(movie_id:int,raw=False):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}'
    params = {
        'include_adult':False,
        'language': 'en-US',
    }
    headers = get_headers()
    response = requests.get(url,headers=headers,params=params)
    
    if raw:
        return response
    
    return response.json()


search_movie('lord of the rings')