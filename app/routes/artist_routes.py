from flask import render_template
from app import app
from app.models.artist import Artist

@app.route("/artists")
def artists_index():
    Artist.delete_all()
    Artist(name="Beastie Boys").save()
    Artist(name="Radiohead").save()
    Artist(name="Photek").save()
    artists = Artist.all()
    return render_template('artists/index.html', title="All Artists", artists=artists)
