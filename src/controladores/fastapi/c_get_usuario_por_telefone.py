from src.interfaces.IRepoUsuario import IArmazenamento
from src.usecases.erros.erros_usecase import ErroInesperado
from src.usecases.uc_get_usuario_por_telefone import UCGetUsuarioPorTelefone
from fastapi import Response, status
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioNaoExiste
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import logging


class CHttpGetUsuarioPorTelefoneFastAPI:
    repo: IArmazenamento
    uc: UCGetUsuarioPorTelefone

    def __init__(self, repo: IArmazenamento):
        self.repo = repo
        self.uc = UCGetUsuarioPorTelefone(self.repo)

    def __call__(self, ddd: int, numero: str):

        try:
            user = self.uc(ddd, numero)
            content = jsonable_encoder(user.__dict__)

            return JSONResponse(content=content, status_code=status.HTTP_200_OK)

        except ErroUsuarioNaoExiste as e:
            return Response(content=str(e), status_code=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            logging.exception(str(ErroInesperado()))
            return Response(content=str(ErroInesperado()), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

