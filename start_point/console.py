# Use this file to test your repository functions 
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

from db.run_sql import show_table, delete_all, find_by_id

# delete contents of album table
# delete contents of artists table


# artist1 = Artist("Foo Fighters")
# artist_repository.save(artist1)

# album1 = Album("The Colour and The Shape", artist1)
# album_repository.save(album1)

# print(show_table("artists"))
# print(show_table("albums"))

# delete_all("albums")
# delete_all("artists")

print(show_table("albums"))
print(show_table("artists"))

print(find_by_id(8, "albums"))