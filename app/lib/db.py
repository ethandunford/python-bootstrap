import psycopg2.extras as extra
import psycopg2 as db
from meta.result import Status, DbResult
from lib.utils import log


class Db(object):

    def __init__(self, configuration: str):
        self.configuration = configuration

    def run_db(self, sql, params=None) -> DbResult:
        try:
            with db.connect(self.configuration) as conn:
                with conn.cursor(cursor_factory=extra.DictCursor) as cx:
                    cx.execute(sql, params)
                    data = cx.fetchall()
                    return DbResult(status=Status.Ok, data=data)
        except Exception as e:
            log("Database error")
            print(e)
            return DbResult(status=Status.Error, error=e)

    def exec_db(self, sql, params=None) -> DbResult:
        try:
            with db.connect(self.configuration) as conn:
                with conn.cursor(cursor_factory=extra.DictCursor) as cx:
                    r = cx.execute(sql, params)
                    return DbResult(status=Status.Ok)
        except Exception as e:
            log("Database error")
            print(e)
            return DbResult(status=Status.Error, error=e)

    def exec_returning_db(self, sql, params=None) -> DbResult:
        try:
            with db.connect(self.configuration) as conn:
                with conn.cursor(cursor_factory=extra.DictCursor) as cx:
                    r = cx.execute(sql, params)
                    return DbResult(status=Status.Ok, data=cx.fetchone()[0])
        except Exception as e:
            log("Database error")
            print(e)
            return DbResult(status=Status.Error, error=e)

