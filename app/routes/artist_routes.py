from flask import render_template
from app import app
from app.models.artist import Artist

@app.route("/artists")
def artists_index():
    artist = Artist("Radiohead")
    return artist.shout_name()
