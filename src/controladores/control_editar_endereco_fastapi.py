from fastapi import Response

from devmaua.src.models.usuario import Usuario
from devmaua.src.models.endereco import Endereco
from devmaua.src.models.erros.erro_usuario import ErroDadosUsuarioInvalidos
from devmaua.src.models.erros.erro_endereco import ErroDadosEnderecoInvalidos

from src.usecases.uc_editar_endereco import UCEditarEndereco

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroEnderecoInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido


class ControllerHTTPEditarEnderecoFastAPI():
    
    def editarEndereco(self, body: dict, editarEnderecoUC: UCEditarEndereco):
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
            usuario = Usuario.criarUsuarioPorDict(body['usuario'])
            endereco = Endereco.criarEnderecoPorDict(body['endereco'])
            
            editarEnderecoUC.editarEndereco(usuario, endereco, body['logradouro'], body['numero'], body['cep'], body['complemento'], body['tipo'])
            response = Response(content="Endereco editado com sucesso", status_code=200)
        
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