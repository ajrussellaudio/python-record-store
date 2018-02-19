from flask import render_template
from app import app
from app.models.album import Album
from app.models.artist import Artist

@app.route("/albums")
def albums_index():
    albums = Album.all()
    return render_template('albums/index.html', albums=albums)

@app.route("/albums/new")
def albums_new():
    artists = Artist.all()
    return render_template('albums/new.html', artists=artists)
