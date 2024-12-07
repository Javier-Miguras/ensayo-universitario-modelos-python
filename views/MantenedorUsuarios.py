from controllers.UsuariosController import UsuariosController
from helpers.validate_helper import validarOpcion
from helpers.validate_helper import cerrarApp

class MantenedorUsuarios:
    def __init__(self):
        self.__controller = UsuariosController()
        self.menu()

    #     controller = UsuariosController()
    #     usuarios = controller.index()
    #     print(usuarios)
        
    def menu(self):
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
            print("crear")
        elif int(opcion_seleccionada) == 2:
            print("listar")
        elif int(opcion_seleccionada) == 3:
            print("actualiar")
        elif int(opcion_seleccionada) == 4:
            print("eliminar")
        elif int(opcion_seleccionada) == 5:
            print("volver")
        else:
            cerrarApp()