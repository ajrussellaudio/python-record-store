from flask import render_template
from app import app

@app.route("/")
def index():
    return render_template('index.html', title='Home', text='Welcome to Big Al\'s Record Store!')

from app.routes import artist_routes
from app.routes import album_routes
