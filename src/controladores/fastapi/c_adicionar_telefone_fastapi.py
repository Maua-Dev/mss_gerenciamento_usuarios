from fastapi import Response, status

from devmaua.src.models.usuario import Usuario
from devmaua.src.models.telefone import Telefone
from devmaua.src.models.erros.erro_usuario import ErroDadosUsuarioInvalidos
from devmaua.src.models.erros.erro_telefone import ErroDadosTelefoneInvalidos

from src.usecases.uc_adicionar_telefone import UCAdicionarTelefone

from src.interfaces.IRepoUsuario import IArmazenamento

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroTelefoneInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioNaoExiste
from src.usecases.erros.erros_usecase import ErroInesperado

import logging


class ControllerHTTPAdicionarTelefoneFastAPI:
    repo: IArmazenamento
    uc: UCAdicionarTelefone

    def __init__(self, repo: IArmazenamento):
        self.repo = repo
        self.uc = UCAdicionarTelefone(self.repo)

    def __call__(self, body: dict):
        """ Estrutura do body:
            {
                "usuario": dict de usuario,
                "telefone": dict de telefone
            }
        
        """
        
        try:
            usuario = Usuario.criarUsuarioPorDict(body['usuario'])
            telefone = Telefone.criarTelefonePorDict(body['telefone'])
            
            self.uc(usuario, telefone)
            return Response(content="Telefone adicionado com sucesso", status_code=status.HTTP_200_OK)
        
        except ErroUsuarioNaoExiste as e:
            return Response(content=str(e), status_code=status.HTTP_404_NOT_FOUND)
            
        except (ErroTelefoneInvalido, ErroDadosUsuarioInvalidos, ErroDadosTelefoneInvalidos, KeyError) as e:
            return Response(content=str(e), status_code=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logging.exception(str(ErroInesperado()))
            return Response(content=str(ErroInesperado()), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
