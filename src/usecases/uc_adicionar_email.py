from devmaua.src.models.email import Email
from devmaua.src.models.usuario import Usuario

from src.interfaces.IRepoUsuario import IArmazenamento

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroEmailInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioNaoExiste


class UCAdicionarEmail():
    
    alteracaoInfosCadastro: IArmazenamento
    
    def __init__(self, alteracaoInfosCadastro: IArmazenamento):
        self.alteracaoInfosCadastro = alteracaoInfosCadastro
        
    def __call__(self, usuario: Usuario, email: Email):
        if not(self.alteracaoInfosCadastro.usuarioExiste(usuario)):
            raise ErroUsuarioNaoExiste
        
        if email == None:
            raise ErroEmailInvalido
        
        self.alteracaoInfosCadastro.adicionarEmail(usuario, email)
        