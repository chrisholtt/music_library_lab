from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository 


def delete_all():
    sql = """
    DELETE FROM albums
    """
    run_sql(sql)

def save(album):
    sql = """
    INSERT INTO albums (title, genre, artist_id)
    VALUES (%s, %s, %s)
    RETURNING *
    """

    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id

    return album



def find_by_id(album_id):
    album_temp = None
    sql = """
    SELECT * FROM albums WHERE id = %s
    """
    values = [album_id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        artist = artist_repository.find_by_id(album_id)
        album_temp = Album(result['title'], result['genre'], artist)
    return album_temp




def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        album = Album(row['title'], row['genre'], row['artist_id'] )
        albums.append(album)
    return albums


def find_albums_by_artist(artist):
    albums = []

    sql = """
    SELECT * FROM albums WHERE artist_id = %s
    """
    values = [artist.id]
    results = run_sql(sql, values)

    for row in results:
        album = Album(row['title'], row['genre'], artist)
        albums.append(album)

    return albums

def delete_from_id(album):
    sql = """
    DELETE FROM albums
    WHERE id = %s
    """

    values = [album.id]
    run_sql(sql, values)

