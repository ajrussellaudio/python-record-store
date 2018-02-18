import psycopg2
from psycopg2.extras import DictCursor

class Artist():
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name')

    def save(self):
        conn = psycopg2.connect('dbname=record-store')
        c = conn.cursor(cursor_factory=DictCursor)
        sql = "INSERT INTO artists (name) VALUES (%s) RETURNING id"
        values = (self.name, )
        c.execute(sql, values)
        self.id = c.fetchone()['id']
        conn.commit()
        conn.close()

    @staticmethod
    def all():
        conn = psycopg2.connect('dbname=record-store')
        c = conn.cursor(cursor_factory=DictCursor)
        sql = "SELECT * FROM artists"
        values = ()
        c.execute(sql, values)
        results = c.fetchall()
        conn.commit()
        conn.close()
        return [Artist(**row) for row in results]
