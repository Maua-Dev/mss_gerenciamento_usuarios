from devmaua.src.models.usuario import Usuario

from src.interfaces.IRepoUsuario import IArmazenamentoUsuario
from src.usecases.erros.erros_uc_alteracao_info_cadastro_usuario import ErroUsuarioNaoExiste
from src.usecases.erros.erros_usecase_usuario import ErroIdInvalido


class UCGetUsuarioPorUserId:
    usuarioRepo: IArmazenamentoUsuario

    def __init__(self, usuarioRepo: IArmazenamentoUsuario):
        self.usuarioRepo = usuarioRepo

    def __call__(self, userId: int) -> Usuario:
        if(userId < 0):
            raise ErroIdInvalido
        #Erro é re-levantado pois repo pode ser alterado
        try:
            return self.usuarioRepo.getUsuarioPorUserId(userId)
        except:
            raise ErroUsuarioNaoExiste