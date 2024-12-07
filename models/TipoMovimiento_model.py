import sqlite3

class TipoMovimiento_model:
    def __init__(self):
        self.__conn = sqlite3.connect("trabajo.db")

    def get(self, id):
        query = self.__conn.execute(f"SELECT * FROM tipo_movimientos WHERE id = {id}")
        data = query.fetchone()
        return data
    
    def getWhere(self, where=''):
        
        if where == '':
            where = '1 > 0'

        query = self.__conn.execute(f"SELECT * FROM tipo_movimientos WHERE {where}")
        data = query.fetchone()
        return data
    
    def getAll(self, where=''):

        if where == '':
            where = '1 > 0'

        try:
            query = self.__conn.execute(f"SELECT * FROM tipo_movimientos WHERE {where}")
            data = query.fetchall()
            return data
        except:
            return False
    
    def insert(self, tipoMovimiento, abono):
        try:
            self.__conn.execute(f"INSERT INTO tipo_movimientos(tipo_movimiento, abono) VALUES ('{tipoMovimiento}', {abono})")
            self.__conn.commit()

            return True
        except:
            return False
        
    def update(self, id, tipoMovimiento, abono):
        try:
            self.__conn.execute(f"UPDATE tipo_movimientos SET tipo_movimiento = '{tipoMovimiento}', abono = {abono} WHERE id = {id}")
            self.__conn.commit()

            return True
        except:
            return False
        
    def delete(self, id):
        try:
            self.__conn.execute(f"DELETE FROM tipo_movimientos WHERE id = {id}")
            self.__conn.commit()

            return True
        except:
            return False