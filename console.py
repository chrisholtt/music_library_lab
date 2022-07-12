import pdb 
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository


album_repository.delete_all()
artist_repository.delete_all()

artist1 = Artist("Tevvez")
artist_repository.save(artist1)

artist2 = Artist("Darren styles")
artist_repository.save(artist2)

album1 = Album("Legend", "Hardstyle", artist1)
album_repository.save(album1)

album2 = Album("Man on the moon", "Hardstyle", artist2)
album_repository.save(album2)

album3 = Album("Quasar", "Hardstyle", artist1)
album_repository.save(album3)



result = [album_repository.find_by_id(album1.id)]
# for thing in result:
#     print(thing.__dict__)

result = artist_repository.select_all()
# for thing in result:
#     print(thing.__dict__)


result = album_repository.find_albums_by_artist(artist1)
for thing in result:
    print(thing.__dict__)


# Updating artist1 name:
artist1.name = 'Not Tevvez'
artist_repository.update(artist1)

album_repository.delete_from_id(album3)



