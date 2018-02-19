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

    def update(self):
        sql = "UPDATE albums SET (title, stock, artist_id) = (%s, %s, %s) WHERE id = %s"
        values = (self.title, self.stock, self.artist_id, self.id)
        SqlQuery.run(sql, values)

    def artist(self):
        from app.models.artist import Artist
        sql = "SELECT * FROM artists WHERE id = %s"
        values = (self.artist_id,)
        result = SqlQuery.run(sql, values)
        return Artist(**result[0])

    def stock_level(self):
        if self.stock > 5:
            return 'high'
        elif self.stock > 2:
            return 'medium'
        else:
            return 'low'

    @staticmethod
    def all():
        sql = "SELECT * FROM albums"
        results = SqlQuery.run(sql)
        return [Album(**row) for row in results]

    @staticmethod
    def find(id):
        sql = "SELECT * FROM albums WHERE id = %s"
        values = (id,)
        result = SqlQuery.run(sql, values)
        return Album(**result[0])

    @staticmethod
    def delete_all():
        sql = "DELETE FROM albums"
        SqlQuery.run(sql)
