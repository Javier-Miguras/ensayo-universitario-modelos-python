import sqlite3

class CtaMovimientoModel:
    def __init__(self):
        self.__conn = sqlite3.connect("trabajo.db")
        self.__id = None
        self.__cuenta_id = None
        self.__tipo_movimiento_id = None
        self.__saldo_previo = None
        self.__monto_movimiento = None
        self.__saldo_final = None
        self.__fecha_movimiento = None
        self.__cuenta_destino_id = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def cuenta_id(self):
        return self.__cuenta_id

    @cuenta_id.setter
    def cuenta_id(self, value):
        self.__cuenta_id = value

    @property
    def tipo_movimiento_id(self):
        return self.__tipo_movimiento_id

    @tipo_movimiento_id.setter
    def tipo_movimiento_id(self, value):
        self.__tipo_movimiento_id = value

    @property
    def saldo_previo(self):
        return self.__saldo_previo

    @saldo_previo.setter
    def saldo_previo(self, value):
        self.__saldo_previo = value

    @property
    def monto_movimiento(self):
        return self.__monto_movimiento

    @monto_movimiento.setter
    def monto_movimiento(self, value):
        self.__monto_movimiento = value

    @property
    def saldo_final(self):
        return self.__saldo_final

    @saldo_final.setter
    def saldo_final(self, value):
        self.__saldo_final = value

    @property
    def fecha_movimiento(self):
        return self.__fecha_movimiento

    @fecha_movimiento.setter
    def fecha_movimiento(self, value):
        self.__fecha_movimiento = value

    @property
    def cuenta_destino_id(self):
        return self.__cuenta_destino_id

    @cuenta_destino_id.setter
    def cuenta_destino_id(self, value):
        self.__cuenta_destino_id = value

    def get(self):
        query = self.__conn.execute(f"SELECT * FROM cuenta_movimientos WHERE id = {self.id}")
        data = query.fetchone()
        return data
    
    def get_where(self, where=''):
        if where == '':
            where = '1 > 0'
        
        query = self.__conn.execute(f"SELECT * FROM cuenta_movimientos WHERE {where}")
        data = query.fetchone()
        return data
    
    def get_all(self, where=''):
        if where == '':
            where = '1 > 0'

        try:
            query = self.__conn.execute(f"SELECT * FROM cuenta_movimientos WHERE {where}")
            data = query.fetchall()
            return data
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    def insert(self):
        try:
            if self.cuenta_destino_id == None:
                cuenta_destino = 'NULL'
            else:
                cuenta_destino = self.cuenta_destino_id
                
            self.__conn.execute(f"""
                INSERT INTO cuenta_movimientos(cuenta_id, tipo_movimiento_id, saldo_previo, monto_movimiento, saldo_final, fecha_movimiento, cuenta_destino_id) 
                VALUES ({self.cuenta_id}, {self.tipo_movimiento_id}, {self.saldo_previo}, {self.monto_movimiento}, {self.saldo_final}, '{self.fecha_movimiento}', {cuenta_destino})
            """)
            self.__conn.commit()
            return True
        except Exception as e:
            print(f"Error al insertar: {e}")
            return False
        
    def update(self):
        try:
            self.__conn.execute(f"""
                UPDATE cuenta_movimientos 
                SET cuenta_id = {self.cuenta_id}, tipo_movimiento_id = {self.tipo_movimiento_id}, saldo_previo = {self.saldo_previo}, 
                monto_movimiento = {self.monto_movimiento}, saldo_final = {self.saldo_final}, fecha_movimiento = '{self.fecha_movimiento}' 
                WHERE id = {self.id}
            """)
            self.__conn.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False
        
    def delete(self):
        try:
            self.__conn.execute(f"DELETE FROM cuenta_movimientos WHERE id = {self.id}")
            self.__conn.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar: {e}")
            return False
