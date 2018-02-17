from flask import render_template
from app import app
from app.models.artist import Artist

@app.route("/artists")
def artists_index():
    artists = [Artist("Radiohead"), Artist("Photek"), Artist("Lightning Bolt"), Artist("Rolling Stones")]
    return render_template('artists/index.html', artists=artists)
