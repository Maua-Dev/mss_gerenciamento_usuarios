from fastapi import Response

from devmaua.src.models.usuario import Usuario
from devmaua.src.models.email import Email
from devmaua.src.models.erros.erro_usuario import ErroDadosUsuarioInvalidos
from devmaua.src.models.erros.erro_email import ErroDadosEmailInvalidos

from src.usecases.uc_remover_email import UCRemoverEmail

from src.interfaces.IRepoUsuario import IArmazenamento

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroEmailInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioNaoExiste
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroManipulacaoEmailFaculdade
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroDeletarEmailUnico

from http import HTTPStatus
import logging


class ControllerHTTPRemoverEmailFastAPI:
    repo: IArmazenamento
    uc: UCRemoverEmail

    def __init__(self, repo: IArmazenamento):
        self.repo = repo
        self.uc = UCRemoverEmail(self.repo)

    def __call__(self, body: dict):
        
        try:
            usuario = Usuario.criarUsuarioPorDict(body['usuario'])
            email = Email.criarEmailPorDict(body['email'])
            
            self.uc(usuario, email)

            return Response(content="Email removido com sucesso", status_code=HTTPStatus.OK)
        
        except ErroUsuarioNaoExiste as e:
            return Response(content=str(e), status_code=HTTPStatus.NOT_FOUND)
            
        except (ErroEmailInvalido, ErroDadosUsuarioInvalidos, ErroDadosEmailInvalidos, KeyError,
                ErroManipulacaoEmailFaculdade, ErroDeletarEmailUnico) as e:

            return Response(content=str(e), status_code=HTTPStatus.BAD_REQUEST)
                        
        except Exception as e:
            logging.exception("Erro inesperado")
            return Response(content="Erro inesperado", status_code=HTTPStatus.INTERNAL_SERVER_ERROR)
