from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album

def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

# def select_all():
#     users = []

#     sql = "SELECT * FROM users"
#     results = run_sql(sql)

#     for row in results:
#         user = User(row['first_name'], row['last_name'], row['id'] )
#         users.append(user)
#     return users