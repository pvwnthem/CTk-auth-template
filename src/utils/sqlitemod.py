import sqlite3 

class SqliteMod:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, columns):
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name}({columns})")
        self.connection.commit()

    def insert(self, table_name, values):
        self.cursor.execute(f"INSERT INTO {table_name} VALUES({values})")
        self.connection.commit()
    
    def select(self, table_name, columns, where=None):
        if where:
            self.cursor.execute(f"SELECT {columns} FROM {table_name} WHERE {where}")
        else:
            self.cursor.execute(f"SELECT {columns} FROM {table_name}")
        return self.cursor.fetchall()

    def update(self, table_name, column, value, where):
        self.cursor.execute(f"UPDATE {table_name} SET {column} = {value} WHERE {where}")
        self.connection.commit()
    
    