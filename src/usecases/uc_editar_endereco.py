from devmaua.src.models.endereco import Endereco
from devmaua.src.models.usuario import Usuario

from devmaua.src.enum.tipo_endereco import TipoEndereco

from src.interfaces.IRepoUsuario import IArmazenamento

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioNaoExiste
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroEnderecoInvalido

from typing import Optional


class UCEditarEndereco():
    
    alteracaoInfosCadastro: IArmazenamento
    
    def __init__(self, alteracaoInfosCadastro: IArmazenamento):
        self.alteracaoInfosCadastro = alteracaoInfosCadastro
        
    def __call__(self, usuario: Usuario, endereco: Endereco, logradouro: Optional[str], numero: Optional[int], cep: Optional[str], complemento: Optional[str], tipo: Optional[TipoEndereco]):
        if not(self.alteracaoInfosCadastro.usuarioExiste(usuario)):
            raise ErroUsuarioNaoExiste
        
        if endereco == None or endereco not in usuario.contato.enderecos:
            raise ErroEnderecoInvalido
        
        self.alteracaoInfosCadastro.editarEndereco(usuario, endereco, logradouro, numero, cep, complemento, tipo)