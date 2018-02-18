from app import app
from app.models.artist import Artist

@app.cli.command("seed_db")
def seed_command():
    print("Seeding...", end=" ")
    Artist.delete_all()
    Artist(name="AC/DC").save()
    Artist(name="Beastie Boys").save()
    Artist(name="Carl Craig").save()
    Artist(name="Deftones").save()
    Artist(name="Eels").save()
    print("done")
