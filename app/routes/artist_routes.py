from flask import render_template
from app import app
from app.models.artist import Artist

@app.route("/artists")
def artists_index():
    artists = Artist.all()
    return render_template('artists/index.html', title="All Artists", artists=artists)

@app.route("/artists/<id>")
def artists_show(id):
    artist = Artist.find(id)
    return render_template('artists/show.html', title=artist.name, artist=artist)
