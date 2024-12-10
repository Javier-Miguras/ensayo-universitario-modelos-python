from models.CtaCorriente_model import CtaCorrienteModel
from models.Usuario_model import UsuarioModel

class CuentaCorrienteController:
    def __init__(self):
        self.__ctaCte_model = CtaCorrienteModel()
        self.__user_model = UsuarioModel()

    def index(self):
        ctaCte = self.__ctaCte_model.get_all()
        return ctaCte
    
    def create(self, numero_cuenta, usuario_id, saldo):
        self.__ctaCte_model.numero_cuenta = numero_cuenta
        self.__ctaCte_model.usuario_id = usuario_id
        self.__ctaCte_model.saldo = saldo

        validate_account = self.__ctaCte_model.get_where(f"numero_cuenta = '{numero_cuenta}'")

        if validate_account:
            raise Exception("Error: corriente no encontrada ya registrada")
        
        try:
            usuario_id = int(usuario_id)
        except:
            raise Exception("Error: formato de id de usuario inválido")
        
        try:
            saldo = int(saldo)
        except:
            raise Exception("Error: formato de saldo inválido")
        
        if saldo < 0:
            raise Exception("Error: saldo inválido")
        
        self.__user_model.id = usuario_id
        validate_user = self.__user_model.get()

        if not validate_user:
            raise Exception("Error: usuario no encontrado")

        if self.__ctaCte_model.insert():
            return True
        else:
            return False
    
    def update(self, id, numero_cuenta, usuario_id, saldo):
        try:
            id = int(id)
        except ValueError:
            raise Exception("Error: formato de ID no válido")

        self.__ctaCte_model.id = id
        ctaCte = self.__ctaCte_model.get()

        if not ctaCte:
            raise Exception("Error: corriente no encontrada no encontrada")

        validate = self.__ctaCte_model.get_all(f"numero_cuenta = '{numero_cuenta}' AND id != {id}")

        if validate:
            raise Exception("Error: Cuenta ya registrado")
        
        try:
            saldo = int(saldo)
        except:
            raise Exception("Error: formato de saldo inválido")
        
        if saldo < 0:
            raise Exception("Error: saldo inválido")
        
        try:
            usuario_id = int(usuario_id)
        except:
            raise Exception("Error: formato de id de usuario inválido")
        
        self.__user_model.id = usuario_id
        validate_user = self.__user_model.get()

        if not validate_user:
            raise Exception("Error: usuario no encontrado")

        self.__ctaCte_model.numero_cuenta = numero_cuenta
        self.__ctaCte_model.usuario_id = usuario_id
        self.__ctaCte_model.saldo = saldo

        if self.__ctaCte_model.update():
            return True
        else:
            return False

    def delete(self, id):
        try:
            id = int(id)
        except ValueError:
            raise Exception("Error: formato de ID no válido")

        self.__ctaCte_model.id = id
        ctaCte = self.__ctaCte_model.get()

        if not ctaCte:
            raise Exception("Error: cuenta corriente no encontrada")

        if self.__ctaCte_model.delete():
            return True
        else:
            return False