import yaml

from lib.db import Db
from data.schema import get_schema
from meta.status import Status
import lib.utils as utils


class Migrate:
    db = Db(utils.get_env("DB"))

    def run(self, _schema: str):
        logo = """
        #       ____________________________________________________
        #      |      __  ____                  __  _               |
        #      |     /  |/  (_)___ __________ _/ /_(_)___  ____     |
        #      |    / /|_/ / / __ `/ ___/ __ `/ __/ / __ \/ __ \    |
        #      |   / /  / / / /_/ / /  / /_/ / /_/ / /_/ / / / /    |
        #      |  /_/  /_/_/\__, /_/   \__,_/\__/_/\____/_/ /_/     |
        #      |           /____/                                   |
        #      |____________________________________________________|
        #      |                                                    |
        #      |         all are schema are belong to us!           |
        #      |____________________________________________________|      
        """

        print(logo)

        try:
            schema = yaml.load(_schema, Loader=yaml.FullLoader)
            remote_tables = self.get_remote_table()
            utils.log("tables:")
            for table in schema.keys():
                utils.log(table)
                # check does this table exist in db? if not create it!
                if remote_tables is not None and table not in set(remote_tables):
                    self.create_table(schema[table], table)
                else:
                    current_fields = self.get_fields(table)
                    for source_field in list(schema[table].keys()):
                        utils.log(f"checking source column: {source_field}")
                        if current_fields is not None and source_field not in set(current_fields):
                            self.create_column(table, source_field, schema[table][source_field])
        except Exception as e:
            utils.log(e)

    def get_remote_table(self):
        utils.log("attempting to load up remote tables")
        res = self.db.run_db("select table_name from information_schema.tables where table_schema = 'public';", None)
        if res.get("status") == Status.Ok and res.get("data"):
            tables = []
            for t in res.get("data"):
                tables.append(str(t[0]))
            return tables
        return []

    def get_fields(self, table: str):
        utils.log(f"getting list of columns for table: {table}")
        params = {"table": table}
        res = self.db.run_db("select column_name from information_schema.columns where table_name = %(table)s;", params)
        if res.get("status") == Status.Ok and res.get("data") is not None:
            fields = []
            for t in res.get("data"):
                fields.append(str(t[0]))
            return fields
        return None

    def create_table(self, table: dict, table_name: str):
        utils.log(f"creating new table: {table_name}")

        idx = 0
        sql = f"create table {table_name} (\n"
        for field in table.keys():
            if idx > 0:
                sql += ","
            sql += f"{field} {table[field]} \n"
            idx += 1
        sql += ");"

        self.db.exec_db(sql, None)

    def create_column(self, table: str, col_name: str, col_type: str):
        utils.log(f"creating new column for table: {table} NEW Column: {col_name}")
        sql = f"alter table {table} add column {col_name} {col_type}"
        self.db.exec_db(sql, None)
