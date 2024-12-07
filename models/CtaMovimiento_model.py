import sqlite3

class CtaMovimiento_model:
    def __init__(self):
        self.__conn = sqlite3.connect("../trabajo.db")

    def get(self, id):
        query = self.__conn.execute(f"SELECT * FROM cuenta_movimientos WHERE id = {id}")
        data = query.fetchone()
        return data
    
    def getWhere(self, where=''):
        
        if where == '':
            where = '1 > 0'

        query = self.__conn.execute(f"SELECT * FROM cuenta_movimientos WHERE {where}")
        data = query.fetchone()
        return data
    
    def getAll(self, where=''):

        if where == '':
            where = '1 > 0'

        try:
            query = self.__conn.execute(f"SELECT * FROM cuenta_movimientos WHERE {where}")
            data = query.fetchall()
            return data
        except:
            return False
    
    def insert(self, numeroCuenta, usuarioId, saldo):
        try:
            self.__conn.execute(f"INSERT INTO cuenta_movimientos(numero_cuenta, usuario_id, saldo) VALUES ('{numeroCuenta}', {usuarioId}, {saldo})")
            self.__conn.commit()

            return True
        except:
            return False
        
    def update(self, id, numeroCuenta, usuarioId, saldo):
        try:
            self.__conn.execute(f"UPDATE cuenta_movimientos SET numero_cuenta = '{numeroCuenta}', usuario_id = '{usuarioId}', saldo = {saldo} WHERE id = {id}")
            self.__conn.commit()

            return True
        except:
            return False
        
    def delete(self, id):
        try:
            self.__conn.execute(f"DELETE FROM cuenta_movimientos WHERE id = {id}")
            self.__conn.commit()

            return True
        except:
            return False