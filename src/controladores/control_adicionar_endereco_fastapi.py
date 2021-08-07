from fastapi import Response

from devmaua.src.models.usuario import Usuario
from devmaua.src.models.endereco import Endereco
from devmaua.src.models.erros.erro_usuario import ErroDadosUsuarioInvalidos
from devmaua.src.models.erros.erro_endereco import ErroDadosEnderecoInvalidos

from src.usecases.uc_adicionar_endereco import UCAdicionarEndereco

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroEnderecoInvalido


class ControllerHTTPAdicionarEnderecoFastAPI():
    
    def adicionarEndereco(self, body: dict, adicionarEnderecoUC: UCAdicionarEndereco):
        """ Estilo do body:
            {
                "usuario": dict de dicionario,
                "endereco": dict de endereco
            }       
        """
        try:
            usuario = Usuario.criarUsuarioPorDict(body['usuario'])
            endereco = Endereco.criarEnderecoPorDict(body['endereco'])
            
            adicionarEnderecoUC.adicionarEndereco(usuario, endereco)
            response = Response(content="Endereco adicionado com sucesso", status_code=200)
        
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