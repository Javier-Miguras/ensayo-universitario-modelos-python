import sqlite3

class TipoMovimientoModel:
    def __init__(self):
        self.__conn = sqlite3.connect("trabajo.db")
        self.__id = None
        self.__tipo_movimiento = None
        self.__abono = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def tipo_movimiento(self):
        return self.__tipo_movimiento

    @tipo_movimiento.setter
    def tipo_movimiento(self, value):
        self.__tipo_movimiento = value

    @property
    def abono(self):
        return self.__abono

    @abono.setter
    def abono(self, value):
        self.__abono = value

    def get(self):
        query = self.__conn.execute(f"SELECT * FROM tipo_movimientos WHERE id = {self.id}")
        data = query.fetchone()
        if data:
            self.tipo_movimiento, self.abono = data[1], data[2]
        return data

    def get_where(self, where=''):
        if where == '':
            where = '1 > 0'
        try:
            query = self.__conn.execute(f"SELECT * FROM tipo_movimientos WHERE {where}")
            data = query.fetchone()
            return data
        except sqlite3.OperationalError as e:
            return e

    def get_all(self, where=''):
        if where == '':
            where = '1 > 0'
        try:
            query = self.__conn.execute(f"SELECT * FROM tipo_movimientos WHERE {where}")
            data = query.fetchall()
            return data
        except sqlite3.OperationalError as e:
            return e

    def insert(self):
        try:
            self.__conn.execute(
                f"INSERT INTO tipo_movimientos (tipo_movimiento, abono) VALUES ('{self.tipo_movimiento}', {self.abono});"
            )
            self.__conn.commit()
            return True
        except Exception as e:
            print(f"Error al insertar: {e}")
            return False

    def update(self):
        try:
            self.__conn.execute(
                f"UPDATE tipo_movimientos SET tipo_movimiento = '{self.tipo_movimiento}', abono = {self.abono} WHERE id = {self.id};"
            )
            self.__conn.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False

    def delete(self):
        try:
            self.__conn.execute(f"DELETE FROM tipo_movimientos WHERE id = {self.id}")
            self.__conn.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar: {e}")
            return False
