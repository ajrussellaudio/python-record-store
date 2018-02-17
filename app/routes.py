from flask import render_template
from app import app
from app.models.artist import Artist

@app.route("/")
def index():
    return render_template('index.html', title='Home', text='Welcome to Big Al\'s Record Store!')

@app.route("/artists")
def artists():
    artist = Artist("Radiohead")
    return artist.shout_name()
