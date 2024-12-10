from models.TipoMovimiento_model import TipoMovimientoModel

class TipoMovimientoController:
    def __init__(self):
        self.__tipoMovimiento_model = TipoMovimientoModel()

    def index(self):
        tipo_movimiento = self.__tipoMovimiento_model.get_all()
        return tipo_movimiento
    
    def create(self, tipo_movimiento, abono):
        self.__tipoMovimiento_model.tipo_movimiento = tipo_movimiento
        self.__tipoMovimiento_model.abono = abono

        try: 
            abono = int(abono)
        except:
            raise Exception("Error: formato de abono no válido")
        
        if abono != 0 and abono != 1:
            raise Exception("Error: formato de abono no válido")

        if self.__tipoMovimiento_model.insert():
            return True
        else:
            return False
    
    def update(self, id, tipo_movimiento, abono):
        try:
            id = int(id)
        except ValueError:
            raise Exception("Error: formato de ID no válido")

        self.__tipoMovimiento_model.id = id
        tipoMovimiento = self.__tipoMovimiento_model.get()

        if not tipoMovimiento:
            raise Exception("Error: Tipo de movimiento no encontrado")

        self.__tipoMovimiento_model.tipo_movimiento = tipo_movimiento
        self.__tipoMovimiento_model.abono = abono

        if self.__tipoMovimiento_model.update():
            return True
        else:
            return False

    def delete(self, id):
        try:
            id = int(id)
        except ValueError:
            raise Exception("Error: formato de ID no válido")

        self.__tipoMovimiento_model.id = id
        tipoMovimiento = self.__tipoMovimiento_model.get()

        if not tipoMovimiento:
            raise Exception("Error: Tipo de movimiento no encontrado")

        if self.__tipoMovimiento_model.delete():
            return True
        else:
            return False