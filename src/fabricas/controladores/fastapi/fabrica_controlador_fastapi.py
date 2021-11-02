from devmaua.src.models.usuario import Usuario
from fastapi import FastAPI

from src.controladores.fastapi.usuario.c_get_usuario_por_userid import CHttpGetUsuarioPorUserIdFastAPI
from src.interfaces.IRepoUsuario import IArmazenamentoUsuario
from src.config.enums.fastapi import *
from src.config.proj_config import ProjConfig
from src.controladores.fastapi.roteadores.roteador import Roteador

from src.controladores.fastapi.usuario.c_adicionar_email_fastapi import ControllerHTTPAdicionarEmailFastAPI
from src.controladores.fastapi.usuario.c_remover_email_fastapi import ControllerHTTPRemoverEmailFastAPI
from src.controladores.fastapi.usuario.c_editar_email_fastapi import ControllerHTTPEditarEmailFastAPI
from src.controladores.fastapi.usuario.c_adicionar_endereco_fastapi import ControllerHTTPAdicionarEnderecoFastAPI
from src.controladores.fastapi.usuario.c_remover_endereco_fastapi import ControllerHTTPRemoverEnderecoFastAPI
from src.controladores.fastapi.usuario.c_editar_endereco_fastapi import ControllerHTTPEditarEnderecoFastAPI
from src.controladores.fastapi.usuario.c_adicionar_telefone_fastapi import ControllerHTTPAdicionarTelefoneFastAPI
from src.controladores.fastapi.usuario.c_remover_telefone_fastapi import ControllerHTTPRemoverTelefoneFastAPI
from src.controladores.fastapi.usuario.c_editar_telefone_fastapi import ControllerHTTPEditarTelefoneFastAPI
from src.controladores.fastapi.usuario.c_deletar_usuario_por_email_fastapi import CDeletarUsuarioPorEmailFastAPI
from src.controladores.fastapi.usuario.c_cadastrar_usuario import ControllerHTTPCadastrarUsuario
from src.controladores.fastapi.usuario.c_get_usuario_por_email import CHttpGetUsuarioPorEmailFastAPI
from src.controladores.fastapi.usuario.c_get_usuario_por_telefone import CHttpGetUsuarioPorTelefoneFastAPI


class FabricaControladorFastapi:
    repo: IArmazenamentoUsuario

    __config__: dict

    protocolo: str
    host: str
    porta: str
    root: str
    url: str

    app: FastAPI

    def __init__(self, repo: IArmazenamentoUsuario):
        self.repo = repo

        self.__config__ = ProjConfig.getFastapi()

        self.protocolo = self.__config__[KEY.PROTOCOLO.value]
        self.host = self.__config__[KEY.HOST.value]
        self.porta = self.__config__[KEY.PORTA.value]
        self.root = self.__config__[KEY.ROOT.value]
        self.url = f'{self.protocolo}://{self.host}:{self.porta}{self.root}'

        self.app = FastAPI()
        self.app.include_router(Roteador(self))

    def adicionarEmail(self, body: dict):
        return ControllerHTTPAdicionarEmailFastAPI(self.repo)(body)

    def removerEmail(self, body: dict):
        return ControllerHTTPRemoverEmailFastAPI(self.repo)(body)

    def editarEmail(self, body: dict):
        return ControllerHTTPEditarEmailFastAPI(self.repo)(body)

    def adicionarEndereco(self, body: dict):
        return ControllerHTTPAdicionarEnderecoFastAPI(self.repo)(body)

    def removerEndereco(self, body: dict):
        return ControllerHTTPRemoverEnderecoFastAPI(self.repo)(body)

    def editarEndereco(self, body: dict):
        return ControllerHTTPEditarEnderecoFastAPI(self.repo)(body)

    def adicionarTelefone(self, body: dict):
        return ControllerHTTPAdicionarTelefoneFastAPI(self.repo)(body)

    def removerTelefone(self, body: dict):
        return ControllerHTTPRemoverTelefoneFastAPI(self.repo)(body)

    def editarTelefone(self, body: dict):
        return ControllerHTTPEditarTelefoneFastAPI(self.repo)(body)

    def cadastrarUsuario(self, body: Usuario):
        return ControllerHTTPCadastrarUsuario(self.repo)(body)

    def deletarUsuarioPorEmail(self, body: dict):
        return CDeletarUsuarioPorEmailFastAPI(self.repo)(body)

    def getUsuarioPorUserId(self, userId: int):
        return CHttpGetUsuarioPorUserIdFastAPI(self.repo)(userId)

    def getUsuarioPorEmail(self, email: str):
        return CHttpGetUsuarioPorEmailFastAPI(self.repo)(email)

    def getUsuarioPorTelefone(self, ddd: int, numero: str):
        return CHttpGetUsuarioPorTelefoneFastAPI(self.repo)(ddd, numero)
