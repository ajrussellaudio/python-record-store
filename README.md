# Big Al's Record Store

A Python implementation of the classic Ruby project.

## How do you run this thing?

* Clone this repository.
* `cd` into the folder you cloned
* Set up a virtual environment, for example:

```bash
python3 -m venv .env
source .env/bin/activate
```

* Install dependencies with `pip`:

```bash
pip install -r requirements.txt
```

* Set `FLASK_APP` environment variable to this app:

```bash
export FLASK_APP=record-store.py
```

* If you want live reloading, set Flask to debug mode:

```bash
export FLASK_DEBUG=1
```

* Create a PostgreSQL database:

```bash
createdb record-store
psql -d record-store -f ./app/db/record-store.sql
```

* Seed the database:

```bash
flask seed_db
```

* Start Flask:

```bash
flask run
```

* Visit [http://localhost:5000/](http://localhost:5000/) in your browser
