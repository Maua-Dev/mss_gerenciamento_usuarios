from devmaua.src.models.usuario import Usuario
from devmaua.src.models.erros.erro_usuario import ErroDadosUsuarioInvalidos
from devmaua.src.models.usuario import Usuario
from fastapi import Response

from src.interfaces.IRepoUsuario import IArmazenamento

from src.usecases.erros.erros_usecase import ErroUsuarioExiste
from src.usecases.uc_cadastrar_usuario import UCCadastrarUsuario

from src.controladores.fastapi.enums.status_code import STATUS_CODE


class ControllerHTTPCadastrarUsuario():

    repo: IArmazenamento

    def __init__(self, repo: IArmazenamento):
        self.repo = repo

    def __call__(self, body: dict):

        try:
            cadastrarUsuarioUC = UCCadastrarUsuario(self.repo)
            usuario = Usuario.criarUsuarioPorDict(body)
            cadastrarUsuarioUC(usuario)
            response = Response(content="Usuario criado com sucesso", status_code=STATUS_CODE.OK.value)

        except ErroDadosUsuarioInvalidos:
            response = Response(content=str(ErroDadosUsuarioInvalidos), status_code=STATUS_CODE.BAD_REQUEST.value)

        except ErroUsuarioExiste:
            response = Response(content=str(ErroUsuarioExiste), status_code=STATUS_CODE.BAD_REQUEST.value)

        return response



