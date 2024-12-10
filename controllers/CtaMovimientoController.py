from models.CtaMovimiento_model import CtaMovimientoModel
from models.CtaCorriente_model import CtaCorrienteModel
from models.Usuario_model import UsuarioModel
from models.TipoMovimiento_model import TipoMovimientoModel
from datetime import datetime

class CuentaMovimientoController:
    def __init__(self):
        self.__ctaMovimiento_model = CtaMovimientoModel()
        self.__ctaCorriente_model = CtaCorrienteModel()
        self.__tipoMovimiento_model = TipoMovimientoModel()

    def index(self):
        ctaMovimiento = self.__ctaMovimiento_model.get_all()
        return ctaMovimiento
    
    def create(self, cuenta_id, tipo_movimiento_id, monto_movimiento):
        try:
            cuenta_id = int(cuenta_id)
        except ValueError:
            raise Exception("Error: formato de ID de cuenta no válido")

        validate_account = self.__ctaCorriente_model.get_where(f"id = '{cuenta_id}'")

        if not validate_account:
            raise Exception("Error: corriente no encontrada")
        
        try:
            tipo_movimiento_id = int(tipo_movimiento_id)
        except:
            raise Exception("Error: formato de id de tipo de movimiento inválido")
        
        validate_type_movement = self.__tipoMovimiento_model.get_where(f"id = '{tipo_movimiento_id}'")

        if not validate_type_movement:
            raise Exception("Error: tipo de movimiento no encontrado")
        
        try:
            monto_movimiento = int(monto_movimiento)
        except:
            raise Exception("Error: formato de monto de movimiento inválido")
        
        if monto_movimiento <= 0:
            raise Exception("Error: Monto de movimiento debe ser mayor a $0")
        
        #si el movimiento está marcado en base de datos que implica terceros se pide acá
        if validate_type_movement[3] == True:
            cuenta_destino_id = input("Ingrese id de cuenta de destino: ")

            try:
                cuenta_destino_id = int(cuenta_destino_id)
            except:
                raise Exception("Error: formato de id de cuenta de destino inválido")

            validate_destiny_account = self.__ctaCorriente_model.get_where(f"id = '{cuenta_destino_id}'")

            if not validate_destiny_account:
                raise Exception("Error: cuenta de destino no encontrada")
            
            self.__ctaMovimiento_model.cuenta_destino_id = cuenta_destino_id

        else :
            self.__ctaMovimiento_model.cuenta_destino_id = None
        
        saldo_previo = validate_account[3]

        if validate_type_movement[2] == False:
            if saldo_previo < monto_movimiento:
                raise Exception("Saldo insuficiente para realizar la transacción")
            
            self.__ctaMovimiento_model.saldo_final = saldo_previo - monto_movimiento 
        else:
            self.__ctaMovimiento_model.saldo_final = saldo_previo + monto_movimiento 
        
        self.__ctaMovimiento_model.cuenta_id = cuenta_id
        self.__ctaMovimiento_model.tipo_movimiento_id = tipo_movimiento_id
        self.__ctaMovimiento_model.monto_movimiento = monto_movimiento
        self.__ctaMovimiento_model.saldo_previo = saldo_previo
        self.__ctaMovimiento_model.fecha_movimiento = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if self.__ctaMovimiento_model.insert():
            self.__ctaCorriente_model.id = validate_account[0]
            self.__ctaCorriente_model.numero_cuenta = validate_account[1]
            self.__ctaCorriente_model.usuario_id = validate_account[2]
            self.__ctaCorriente_model.saldo = self.__ctaMovimiento_model.saldo_final
            self.__ctaCorriente_model.update()

            if validate_type_movement[3] == True:
                self.__ctaCorriente_model.id = validate_destiny_account[0]
                self.__ctaCorriente_model.numero_cuenta = validate_destiny_account[1]
                self.__ctaCorriente_model.usuario_id = validate_destiny_account[2]
                self.__ctaCorriente_model.saldo = validate_destiny_account[3] + monto_movimiento
                self.__ctaCorriente_model.update()

            return True
        else:
            return False