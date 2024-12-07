import sqlite3

class Usuario_model:
    def __init__(self):
        self.__conn = sqlite3.connect("trabajo.db")

    def get(self, id):
        query = self.__conn.execute(f"SELECT * FROM usuarios WHERE id = {id}")
        data = query.fetchone()
        return data
    
    def getWhere(self, where=''):
        
        if where == '':
            where = '1 > 0'

        query = self.__conn.execute(f"SELECT * FROM usuarios WHERE {where}")
        data = query.fetchone()
        return data
    
    def getAll(self, where=''):
        if where == '':
            where = '1 > 0'

        try:
            query = self.__conn.execute(f"SELECT * FROM usuarios WHERE {where}")
            data = query.fetchall()
            return data
        except:
            return False
    
    def insert(self, nombre, rut):
        try:
            self.__conn.execute(f"INSERT INTO usuarios(nombre, rut) VALUES ('{nombre}', '{rut}');")
            self.__conn.commit()

            return True
        except:
            return False
        
    def update(self, id, name, rut):
        try:
            self.__conn.execute(f"UPDATE usuarios SET rut = '{rut}', nombre = '{name}' WHERE id = {id}")
            self.__conn.commit()

            return True
        except:
            return False
        
    def delete(self, id):
        try:
            self.__conn.execute(f"DELETE FROM usuarios WHERE id = {id}")
            self.__conn.commit()

            return True
        except:
            return False