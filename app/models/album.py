from app.models.SqlQuery import SqlQuery

class Album:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.title = kwargs.get('title')
        self.stock = kwargs.get('stock', 0)
        self.artist_id = kwargs.get('artist_id')

    def save(self):
        sql = "INSERT INTO albums (title, stock, artist_id) VALUES (%s, %s, %s) RETURNING id"
        values = (self.title, self.stock, self.artist_id)
        result = SqlQuery.run(sql, values)
        self.id = result[0]['id']

    @staticmethod
    def all():
        sql = "SELECT * FROM albums"
        results = SqlQuery.run(sql)
        return [Album(**row) for row in results]

    @staticmethod
    def delete_all():
        sql = "DELETE FROM albums"
        SqlQuery.run(sql)
