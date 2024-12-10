from controllers.UsuariosController import UsuariosController
from helpers.validate_helper import validarOpcion
from helpers.validate_helper import cerrarApp

class MantenedorUsuarios:
    def __init__(self, main_menu):
        self.__controller = UsuariosController()
        self.__main_menu = main_menu
        self.menu()
        
    def menu(self):
        while True:
            print("""
            ==========================
            Mantenedor de Usuarios
            ==========================
            1. Crear un nuevo usuario
            2. Ver todos los usuarios
            3. Actualizar usuario
            4. Eliminar usuario
            5. Volver al menú principal
            0. Salir
            ==========================
            """)

            opcion_seleccionada = input("Seleccione una opción: ")
            
            while not validarOpcion(opcion_seleccionada, 0, 5):
                opcion_seleccionada = input("Opción inválida, vuelva a intentar: ")

            if int(opcion_seleccionada) == 1:

                nombre = input("Ingrese nombre de usuario: ")
                rut = input("Ingrese Rut de usuario: ")

                try:
                    if (UsuariosController().create(nombre, rut)):
                        print("Usuario creado correctamente.")
                    else :
                        print("Error al crear usuario.")
                except Exception as e:
                    print(e)
                continue

            elif int(opcion_seleccionada) == 2:
                print(UsuariosController().index())
                continue
                
            elif int(opcion_seleccionada) == 3:
                id = input("Ingrese id de usuario: ")
                nombre = input("Ingrese nombre de usuario: ")
                rut = input("Ingrese Rut de usuario: ")

                try:
                    if (UsuariosController().update(id, nombre, rut)):
                        print("Usuario actualizado correctamente.")
                    else :
                        print("Error al actualizar usuario.")
                except Exception as e:
                    print(e)
                continue

            elif int(opcion_seleccionada) == 4:
                id = input("Ingrese id de usuario: ")

                try:
                    if (UsuariosController().delete(id)):
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