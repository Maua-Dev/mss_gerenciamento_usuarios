from fastapi import Response

from devmaua.src.models.usuario import Usuario
from devmaua.src.models.endereco import Endereco
from devmaua.src.models.erros.erro_usuario import ErroDadosUsuarioInvalidos
from devmaua.src.models.erros.erro_endereco import ErroDadosEnderecoInvalidos

from src.usecases.uc_editar_endereco import UCEditarEndereco

from src.interfaces.IRepoUsuario import IArmazenamento

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroEnderecoInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido

from src.controladores.fastapi.enums.status_code import STATUS_CODE


class ControllerHTTPEditarEnderecoFastAPI():

    repo: IArmazenamento

    def __init__(self, repo: IArmazenamento):
        self.repo = repo

    def __call__(self, body: dict):
        """ Estrutura do body:
            {
                "usuario": dict de usuario,
                "endereco": dict de endereco,
                "logradouro": Optional[str],
                "numero": Optional[int],
                "cep": Optional[str],
                "complemento": Optional[str],
                "tipo": Optional[TipoEndereco]
            }
        """
        
        try:
            editarEnderecoUC = UCEditarEndereco(self.repo)
            usuario = Usuario.criarUsuarioPorDict(body['usuario'])
            endereco = Endereco.criarEnderecoPorDict(body['endereco'])
            
            editarEnderecoUC(usuario, endereco, body['logradouro'], body['numero'], body['cep'], body['complemento'], body['tipo'])
            response = Response(content="Endereco editado com sucesso", status_code=STATUS_CODE.OK.value)
        
        except ErroUsuarioInvalido:
            response = Response(content=str(ErroUsuarioInvalido), status_code=STATUS_CODE.BAD_REQUEST.value)
            
        except ErroEnderecoInvalido:
            response = Response(content=str(ErroEnderecoInvalido), status_code=STATUS_CODE.BAD_REQUEST.value)
            
        except ErroDadosUsuarioInvalidos:
            response = Response(content=str(ErroDadosUsuarioInvalidos), status_code=STATUS_CODE.BAD_REQUEST.value)
            
        except ErroDadosEnderecoInvalidos:
            response = Response(content=str(ErroDadosEnderecoInvalidos), status_code=STATUS_CODE.BAD_REQUEST.value)
            
        except KeyError:
            response = Response(content=str(KeyError), status_code=STATUS_CODE.BAD_REQUEST.value)
                            
        return response