from flask import render_template
from app import app
from app.models.album import Album

@app.route("/albums")
def albums_index():
    albums = Album.all()
    return render_template('albums/index.html', albums=albums)
