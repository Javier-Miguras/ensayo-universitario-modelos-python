from controllers.CtaMovimientoController import CuentaMovimientoController
from helpers.validate_helper import validarOpcion
from helpers.validate_helper import cerrarApp

class MenuTransacciones:
    def __init__(self, main_menu):
        self.__controller = CuentaMovimientoController()
        self.__main_menu = main_menu
        self.menu()
        
    def menu(self):
        while True:
            print("""
            ==========================
            Menú de Transacciones
            ==========================
            1. Nuevo Movimiento
            2. Ver todos los movimientos
            3. Buscar movimiento
            4. Generar reporte
            5. Volver al menú principal
            0. Salir
            ==========================
            """)

            opcion_seleccionada = input("Seleccione una opción: ")
            
            while not validarOpcion(opcion_seleccionada, 0, 5):
                opcion_seleccionada = input("Opción inválida, vuelva a intentar: ")

            if int(opcion_seleccionada) == 1:

                cuenta_id = input("Ingrese id de la cuenta de origen: ")
                tipo_movimiento_id = input("Ingrese id del tipo de movimiento: ")
                monto_movimiento = input("Ingrese monto del movimiento: ")

                try:
                    if (CuentaMovimientoController().create(cuenta_id, tipo_movimiento_id, monto_movimiento)):
                        print("Transacción bancaria ejecutada correctamente.")
                    else :
                        print("Error al crear transacción bancaria.")
                except Exception as e:
                    print(e)
                continue

            elif int(opcion_seleccionada) == 2:
                print(CuentaMovimientoController().index())
                continue
                
            elif int(opcion_seleccionada) == 3:
                id = input("Ingrese id de usuario: ")
                nombre = input("Ingrese nombre de usuario: ")
                rut = input("Ingrese Rut de usuario: ")

                try:
                    if (CuentaMovimientoController().update(id, nombre, rut)):
                        print("Usuario actualizado correctamente.")
                    else :
                        print("Error al actualizar usuario.")
                except Exception as e:
                    print(e)
                continue

            elif int(opcion_seleccionada) == 4:
                id = input("Ingrese id de usuario: ")

                try:
                    if (CuentaMovimientoController().delete(id)):
                        print("Usuario eliminado correctamente.")
                    else :
                        print("Error al eliminar usuario.")
                except Exception as e:
                    print(e)
                continue

            elif int(opcion_seleccionada) == 5:
                self.__main_menu()

            else:
                cerrarApp()