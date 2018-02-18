import psycopg2
from psycopg2.extras import DictCursor

class SqlQuery:
    @staticmethod
    def run(sql, values = ()):
        result = None
        conn = psycopg2.connect('dbname=record-store')
        c = conn.cursor(cursor_factory=DictCursor)
        c.execute(sql, values)
        if c.description:
            result = c.fetchall()
        conn.commit()
        conn.close()
        return result
