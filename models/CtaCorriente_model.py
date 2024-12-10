import sqlite3

class CtaCorrienteModel:
    def __init__(self):
        self.__conn = sqlite3.connect("trabajo.db")
        self.__id = None
        self.__numero_cuenta = None
        self.__usuario_id = None
        self.__saldo = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def numero_cuenta(self):
        return self.__numero_cuenta

    @numero_cuenta.setter
    def numero_cuenta(self, value):
        self.__numero_cuenta = value

    @property
    def usuario_id(self):
        return self.__usuario_id

    @usuario_id.setter
    def usuario_id(self, value):
        self.__usuario_id = value

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        self.__saldo = value

    def get(self):
        query = self.__conn.execute(f"SELECT * FROM ctas_corrientes WHERE id = {self.id}")
        data = query.fetchone()
        return data

    def get_where(self, where=''):
        if where == '':
            where = '1 > 0'
        try:
            query = self.__conn.execute(f"SELECT * FROM ctas_corrientes WHERE {where}")
            data = query.fetchone()
            return data
        except sqlite3.OperationalError as e:
            return e

    def get_all(self, where=''):
        if where == '':
            where = '1 > 0'

        try:
            query = self.__conn.execute(f"SELECT * FROM ctas_corrientes WHERE {where}")
            data = query.fetchall()
            return data
        except sqlite3.OperationalError as e:
            return e

    def insert(self):
        try:
            self.__conn.execute(
                f"INSERT INTO ctas_corrientes (numero_cuenta, usuario_id, saldo) VALUES ('{self.numero_cuenta}', {self.usuario_id}, {self.saldo});"
            )
            self.__conn.commit()
            return True
        except Exception as e:
            print(f"Error al insertar: {e}")
            return False

    def update(self):
        try:
            self.__conn.execute(
                f"UPDATE ctas_corrientes SET numero_cuenta = '{self.numero_cuenta}', usuario_id = {self.usuario_id}, saldo = {self.saldo} WHERE id = {self.id}"
            )
            self.__conn.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False

    def delete(self):
        try:
            self.__conn.execute(f"DELETE FROM ctas_corrientes WHERE id = {self.id}")
            self.__conn.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar: {e}")
            return False
