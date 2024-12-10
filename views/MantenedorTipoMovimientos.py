from controllers.TipoMovimientoController import TipoMovimientoController
from helpers.validate_helper import validarOpcion
from helpers.validate_helper import cerrarApp

class MantenedorTipoMovimientos:
    def __init__(self, main_menu):
        self.__controller = TipoMovimientoController()
        self.__main_menu = main_menu
        self.menu()
        
    def menu(self):
        while True:
            print("""
            =====================================
            Mantenedor de tipos de movimientos
            =====================================
            1. Crear un nuevo tipo de movimiento
            2. Ver todos los tipos de movimientos
            3. Actualizar tipo de movimiento
            4. Eliminar tipo de movimiento
            5. Volver al menú principal
            0. Salir
            =====================================
            """)

            opcion_seleccionada = input("Seleccione una opción: ")
            
            while not validarOpcion(opcion_seleccionada, 0, 5):
                opcion_seleccionada = input("Opción inválida, vuelva a intentar: ")

            if int(opcion_seleccionada) == 1:

                tipo_movimiento = input("Nombre de tipo de movimiento: ")
                abono = input("¿Es abono o cargo? ingrese 1 para abono y 0 para cargo: ")

                try:
                    if (TipoMovimientoController().create(tipo_movimiento, abono)):
                        print("Tipo de movimiento creado correctamente.")
                    else :
                        print("Error al crear tipo de movimiento.")
                except Exception as e:
                    print(e)
                continue

            elif int(opcion_seleccionada) == 2:
                print(TipoMovimientoController().index())
                continue
                
            elif int(opcion_seleccionada) == 3:
                id = input("Ingrese id de tipo de movimiento: ")
                tipo_movimiento = input("Nombre de tipo de movimiento: ")
                abono = input("¿Es abono o cargo? ingrese 1 para abono y 0 para cargo: ")

                try:
                    if (TipoMovimientoController().update(id, tipo_movimiento, abono)):
                        print("Tipo de movimiento actualizado correctamente.")
                    else :
                        print("Error al actualizar tipo de movimiento.")
                except Exception as e:
                    print(e)
                continue

            elif int(opcion_seleccionada) == 4:
                id = input("Ingrese id de tipo de movimiento: ")

                try:
                    if (TipoMovimientoController().delete(id)):
                        print("Tipo de movimiento eliminado correctamente.")
                    else :
                        print("Error al eliminar tipo de movimiento.")
                except Exception as e:
                    print(e)
                continue

            elif int(opcion_seleccionada) == 5:
                self.__main_menu()

            else:
                cerrarApp()