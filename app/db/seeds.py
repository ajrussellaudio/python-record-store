from app import app
from app.models.artist import Artist

@app.cli.command("seed_db")
def seed_command():
    print("Seeding...", end=" ")
    Artist.delete_all()
    artist_a = Artist(name="At the Drive-In").save()
    artist_b = Artist(name="Beastie Boys").save()
    artist_c = Artist(name="Chemical Brothers").save()
    artist_d = Artist(name="Deftones").save()
    artist_e = Artist(name="Eels").save()
    print("done")
