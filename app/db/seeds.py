from app import app
from app.models.artist import Artist
from app.models.album import Album

@app.cli.command("seed_db")
def seed_command():
    print("Seeding...", end=" ")
    Album.delete_all()
    Artist.delete_all()

    artist_a = Artist(name="At the Drive-In")
    artist_a.save()
    artist_b = Artist(name="Beastie Boys")
    artist_b.save()
    artist_c = Artist(name="Chemical Brothers")
    artist_c.save()
    artist_d = Artist(name="Deftones")
    artist_d.save()
    artist_e = Artist(name="Eels")
    artist_e.save()

    album_1 = Album(title="Relationship of Command", artist_id=artist_a.id)
    album_1.save()
    album_2 = Album(title="Check Your Head", artist_id=artist_b.id)
    album_2.save()
    album_3 = Album(title="Ill Communication", artist_id=artist_b.id)
    album_3.save()
    print("done")
