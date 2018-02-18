from app import app
from app.models.artist import Artist
from app.models.album import Album

@app.cli.command("seed_db")
def seed_command():
    print("Seeding...", end=" ")
    Album.delete_all()
    Artist.delete_all()

    atdi = Artist(name="At the Drive-In")
    atdi.save()
    beasties = Artist(name="Beastie Boys")
    beasties.save()
    chembros = Artist(name="Chemical Brothers")
    chembros.save()
    deftones = Artist(name="Deftones")
    deftones.save()
    eels = Artist(name="Eels")
    eels.save()

    album_1 = Album(title="Relationship of Command", artist_id=atdi.id)
    album_1.save()
    album_2 = Album(title="Check Your Head", artist_id=beasties.id)
    album_2.save()
    album_3 = Album(title="Ill Communication", artist_id=beasties.id)
    album_3.save()
    album_4 = Album(title="Hello Nasty", artist_id=beasties.id)
    album_4.save()
    album_5 = Album(title="Dig Your Own Hole", artist_id=chembros.id)
    album_5.save()
    album_6 = Album(title="Around the Fur", artist_id=deftones.id)
    album_6.save()
    album_7 = Album(title="White Pony", artist_id=deftones.id)
    album_7.save()
    album_8 = Album(title="My Beloved Monster", artist_id=eels.id)
    album_8.save()
    print("done")
