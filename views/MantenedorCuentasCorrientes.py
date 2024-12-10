from controllers.CuentaCorrienteController import CuentaCorrienteController
from helpers.validate_helper import validarOpcion
from helpers.validate_helper import cerrarApp

class MantenedorCuentasCorrientes:
    def __init__(self, main_menu):
        self.__controller = CuentaCorrienteController()
        self.__main_menu = main_menu
        self.menu()
        
    def menu(self):
        while True:
            print("""
            ===================================
            Mantenedor de Ctas Corrientes
            ===================================
            1. Crear una nueva cuenta corriente
            2. Ver todas las cuentas corrientes
            3. Actualizar cuenta corriente
            4. Eliminar cuenta corriente
            5. Volver al menú principal
            0. Salir
            ===================================
            """)

            opcion_seleccionada = input("Seleccione una opción: ")
            
            while not validarOpcion(opcion_seleccionada, 0, 5):
                opcion_seleccionada = input("Opción inválida, vuelva a intentar: ")

            if int(opcion_seleccionada) == 1:

                numero_cuenta = input("Ingrese numero de cuenta: ")
                usuario_id = input("Ingrese id de usuario: ")
                saldo = input("Ingrese saldo inicial: ")


                try:
                    if (CuentaCorrienteController().create(numero_cuenta, usuario_id, saldo)):
                        print("Cuenta corriente creada correctamente.")
                    else :
                        print("Error al crear cuenta corriente.")
                except Exception as e:
                    print(e)
                continue

            elif int(opcion_seleccionada) == 2:
                print(CuentaCorrienteController().index())
                continue
                
            elif int(opcion_seleccionada) == 3:
                id = input("Ingrese id de cuenta: ")
                numero_cuenta = input("Ingrese numero de cuenta: ")
                usuario_id = input("Ingrese id de usuario: ")
                saldo = input("Ingrese saldo inicial: ")

                try:
                    if (CuentaCorrienteController().update(id, numero_cuenta, usuario_id, saldo)):
                        print("Cuenta corriente actualizada correctamente.")
                    else :
                        print("Error al actualizar cuenta corriente.")
                except Exception as e:
                    print(e)
                continue

            elif int(opcion_seleccionada) == 4:
                id = input("Ingrese id de cuenta corriente: ")

                try:
                    if (CuentaCorrienteController().delete(id)):
                        print("cuenta corriente eliminada correctamente.")
                    else :
                        print("Error al eliminar cuenta corriente.")
                except Exception as e:
                    print(e)
                continue

            elif int(opcion_seleccionada) == 5:
                self.__main_menu()

            else:
                cerrarApp()