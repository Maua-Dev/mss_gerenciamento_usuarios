from devmaua.src.models.usuario import Usuario

from src.interfaces.IRepoUsuario import IArmazenamento
from src.usecases.erros.erros_usecase import ErroUsuarioExiste


class UCCadastrarUsuario():

    usuariosRepo: IArmazenamento

    def __init__(self, usuariosRepo: IArmazenamento):
        self.usuariosRepo = usuariosRepo

    def __call__(self, usuario: Usuario):
        if self.usuariosRepo.usuarioExiste(usuario):
            raise ErroUsuarioExiste
        self.usuariosRepo.cadastrarUsuario(usuario)

