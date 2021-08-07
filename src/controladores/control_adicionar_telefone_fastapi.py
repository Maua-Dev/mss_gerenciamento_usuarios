from fastapi import Response

from devmaua.src.models.usuario import Usuario
from devmaua.src.models.telefone import Telefone
from devmaua.src.models.erros.erro_usuario import ErroDadosUsuarioInvalidos
from devmaua.src.models.erros.erro_telefone import ErroDadosTelefoneInvalidos

from src.usecases.uc_adicionar_telefone import UCAdicionarTelefone

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroTelefoneInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido

class ControllerHTTPAdicionarTelefoneFastAPI():
    
    def adicionarTelefone(self, body: dict, adicionarTelefoneUC: UCAdicionarTelefone):
        """ Estrutura do body:
            {
                "usuario": dict de usuario,
                "telefone": dict de telefone
            }
        
        """
        
        try:
            usuario = Usuario.criarUsuarioPorDict(body['usuario'])
            telefone = Telefone.criarTelefonePorDict(body['telefone'])
            
            adicionarTelefoneUC.adicionarTelefone(usuario, telefone)
            response = Response(content="Telefone adicionado com sucesso", status_code=200)
        
        except ErroUsuarioInvalido:
            response = Response(content=str(ErroUsuarioInvalido), status_code=400)
            
        except ErroTelefoneInvalido:
            response = Response(content=str(ErroTelefoneInvalido), status_code=400)
            
        except ErroDadosUsuarioInvalidos:
            response = Response(content=str(ErroDadosUsuarioInvalidos), status_code=400)
            
        except ErroDadosTelefoneInvalidos:
            response = Response(content=str(ErroDadosTelefoneInvalidos), status_code=400)
            
        except KeyError:
            response = Response(content=str(KeyError), status_code=400)
            
        return response