from app.models.SqlQuery import SqlQuery


class Artist():
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name')

    def save(self):
        sql = "INSERT INTO artists (name) VALUES (%s) RETURNING id"
        values = (self.name, )
        result = SqlQuery.run(sql, values)
        self.id = result[0]['id']

    def albums(self):
        from app.models.album import Album
        sql = "SELECT * FROM albums WHERE artist_id = %s"
        values = (self.id,)
        results = SqlQuery.run(sql, values)
        return [Album(**row) for row in results]

    @staticmethod
    def all():
        sql = "SELECT * FROM artists"
        results = SqlQuery.run(sql)
        return [Artist(**row) for row in results]

    @staticmethod
    def find(id):
        sql = "SELECT * FROM artists WHERE id = %s"
        values = (id,)
        result = SqlQuery.run(sql, values)
        return Artist(**result[0])

    @staticmethod
    def delete_all():
        sql = "DELETE FROM artists"
        SqlQuery.run(sql)
