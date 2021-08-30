from fastapi import Response

from devmaua.src.models.usuario import Usuario
from devmaua.src.models.endereco import Endereco
from devmaua.src.models.erros.erro_usuario import ErroDadosUsuarioInvalidos
from devmaua.src.models.erros.erro_endereco import ErroDadosEnderecoInvalidos

from src.usecases.uc_remover_endereco import UCRemoverEndereco

from src.interfaces.interface_alteracao_infos_cadastro import IAlteracaoInfosCadastro

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroEnderecoInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido

class ControllerHTTPRemoverEnderecoFastAPI():

    repo: IAlteracaoInfosCadastro

    def __init__(self, repo: IAlteracaoInfosCadastro):
        self.repo = repo

    def __call__(self, body: dict):
        """ Estrutura do body:
            {
                "usuario": dict de usuario,
                "endereco": dict de endereco
            }
        
        """
        
        try:
            removerEnderecoUC = UCRemoverEndereco(self.repo)
            usuario = Usuario.criarUsuarioPorDict(body['usuario'])
            endereco = Endereco.criarEnderecoPorDict(body['endereco'])
            
            removerEnderecoUC(usuario, endereco)
            response = Response(content="Endereco removido com sucesso", status_code=200)
        
        except ErroUsuarioInvalido:
            response = Response(content=str(ErroUsuarioInvalido), status_code=400)
            
        except ErroEnderecoInvalido:
            response = Response(content=str(ErroEnderecoInvalido), status_code=400)
            
        except ErroDadosUsuarioInvalidos:
            response = Response(content=str(ErroDadosUsuarioInvalidos), status_code=400)
            
        except ErroDadosEnderecoInvalidos:
            response = Response(content=str(ErroDadosEnderecoInvalidos), status_code=400)
            
        except KeyError:
            response = Response(content=str(KeyError), status_code=400)
                        
        return response