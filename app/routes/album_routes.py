from flask import render_template, request, redirect
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

@app.route("/albums", methods=["POST"])
def albums_create():
    album = Album(**request.form.to_dict())
    album.save()
    return redirect("/albums")

@app.route("/albums/<id>")
def albums_show(id):
    album = Album.find(id)
    return render_template('albums/show.html', album=album)

@app.route("/albums/<id>/edit")
def albums_edit(id):
    album = Album.find(id)
    artists = Artist.all()
    return render_template('albums/edit.html', album=album, artists=artists)

@app.route("/albums/<id>/update", methods=["POST"])
def albums_update(id):
    album = Album(**request.form.to_dict(), id=id)
    album.update()
    return redirect("/albums/" + id)
