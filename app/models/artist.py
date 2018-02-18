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

    @staticmethod
    def all():
        sql = "SELECT * FROM artists"
        results = SqlQuery.run(sql)
        return [Artist(**row) for row in results]

    @staticmethod
    def delete_all():
        sql = "DELETE FROM artists"
        SqlQuery.run(sql)
