from .models import Gist
from datetime import datetime

# refactor: https://stackoverflow.com/questions/37041114/python-nested-try-except-vs-if-elif-else#37041169

def operator(value):
    pass

def search_gists(db_connection, **kwargs):
    '''search without params returns all gists'''
    # query = "SELECT * FROM gists WHERE {0}{1}{2}".format(column, operator='=', value)
    
    if not kwargs:
        gists = db_connection.execute("SELECT * FROM gists;")
        for gist in gists:
            yield Gist(gist)
            
    elif 'created_at__gt' in kwargs:
        params = {'created_at': kwargs['created_at__gt']}
        # gists = db_connection.execute(query, params)
        gists = db_connection.execute("SELECT * FROM gists WHERE created_at>=:created_at;", params)
        for gist in gists:
            yield Gist(gist)
            
    elif 'created_at__gte' in kwargs:
        params = {'created_at': kwargs['created_at__gte']}
        gists = db_connection.execute("SELECT * FROM gists WHERE created_at>=:created_at;", params)
        for gist in gists:
            yield Gist(gist)     
    
    elif 'created_at__lt' in kwargs:
        params = {'created_at': kwargs['created_at__lt']}
        gists = db_connection.execute("SELECT * FROM gists WHERE created_at<:created_at;", params)
        for gist in gists:
            yield Gist(gist)   
         
    elif 'created_at__lte' in kwargs:
        if 'github_id' in kwargs:
            params = {'created_at': kwargs['created_at__lte']
                     ,'github_id': kwargs['github_id']
            }
            gists = db_connection.execute("SELECT * FROM gists WHERE created_at<=:created_at and github_id=:github_id;", params)
            for gist in gists:
                yield Gist(gist)
                
        elif 'updated_at__gte' in kwargs:
            params = {'created_at': kwargs['created_at__lte']
                     ,'updated_at': kwargs['updated_at__gte']        
            }
            gists = db_connection.execute("SELECT * FROM gists WHERE datetime(created_at)<=datetime(:created_at) and datetime(updated_at)>=datetime(:updated_at);", params)
            for gist in gists:
                yield Gist(gist)
        
        else:
            params = {'created_at': kwargs['created_at__lte']}
            gists = db_connection.execute("SELECT * FROM gists WHERE datetime(created_at)<=datetime(:created_at);", params)
            for gist in gists:
                yield Gist(gist)

    if 'github_id' in kwargs:
        params = {'github_id': kwargs['github_id']}
        gists = db_connection.execute("SELECT * FROM gists WHERE github_id=:github_id;", params)
        for gist in gists:
            yield Gist(gist)  
    
def build_query():
    pass