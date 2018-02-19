from flask import render_template, request, redirect
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

@app.route("/artists/new")
def artists_new():
    return render_template('artists/new.html')

@app.route("/artists", methods=["POST"])
def artists_create():
    artist = Artist(**request.form.to_dict())
    artist.save()
    return redirect("/artists")
