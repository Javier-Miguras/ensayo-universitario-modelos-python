from models.Usuario_model import Usuario_model

class UsuariosController:
    def __init__(self):
        pass

    def index(self):
        usuarios = Usuario_model().getAll()
        return usuarios