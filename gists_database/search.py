from .models import Gist
from datetime import datetime
import sqlite3


def search_gists(db_connection, **kwargs):
    '''
    for kwarg,value in kwargs.items():
        if isinstance(value,datetime):
            blah = db_connection.execute("SELECT * FROM gists WHERE datetime({}) == datetime(:{})"".format(kwarg,kwarg))
        else:
            blah = db_connection.execute("SELECT * FROM gists WHERE {} = :{}".format(kwarg,kwarg))
        result = [Gist(gist) for gist in blah]
    return result
'''
    query = '''
        SELECT * FROM gists '''

    for kwarg, value in kwargs.items():
        if isinstance(value, datetime):
            query = query + 'WHERE datetime({}) == datetime(:{})'.format(kwarg, kwarg)
        else:
            query = query + 'WHERE {} = :{}'.format(kwarg, kwarg)
    cursor = db_connection.execute(query, kwargs)
    results = [Gist(gist) for gist in cursor]
    return results
