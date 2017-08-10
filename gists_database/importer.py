import requests
import sqlite3
import os.path
import pprint
# source: http://bit.ly/2vLbHSM
# package_dir = os.path.abspath(os.path.dirname(__file__))
# database_path = os.path.join(package_dir, 'gists.db')

# db = sqlite3.connect('database_path')
# cursor = db.execute("SELECT * FROM gists")
# results = cursor.fetchall()
# print(results)

# db.commit()


def import_gists_to_database(db, username, commit=True):
    r = requests.get('https://api.github.com/users/{}/gists'.format(username))
    if r.status_code == 404:
        raise requests.exceptions.HTTPError()
    gists = r.json()
    
    # source https://youtu.be/WRgU4KE66Ag?t=1h9m3s
    query = """INSERT INTO gists (
        github_id, html_url, git_pull_url, git_push_url, commits_url, forks_url, public, created_at, updated_at, comments, comments_url)
        VALUES (
            :github_id, :html_url, :git_pull_url, :git_push_url, :commits_url, :forks_url, :public, :created_at, :updated_at, :comments, :comments_url
            );"""

    for record in gists:
        params = { 'github_id': record['id']
              , 'html_url': record['html_url'] 
              , 'git_pull_url': record['git_pull_url']
              , 'git_push_url': record['git_push_url']
              , 'commits_url': record['commits_url']
              , 'forks_url': record['forks_url']
              , 'public': record['public']
              , 'created_at': record['created_at']
              , 'updated_at': record['updated_at']
              , 'comments': record['comments']
              , 'comments_url': record['comments_url']}
        db.execute(query, params)
        if commit: 
            db.commit()
        
# username = 'gvanrossum'
# import_gists_to_database(db, username)
