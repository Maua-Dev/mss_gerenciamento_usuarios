from devmaua.src.models.email import Email
from devmaua.src.models.usuario import Usuario

from devmaua.src.enum.tipo_email import TipoEmail

from src.interfaces.IRepoUsuario import IArmazenamento

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroEmailInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioNaoExiste
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroManipulacaoEmailFaculdade
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroDeletarEmailUnico


class UCRemoverEmail():
    
    alteracaoInfosCadastro: IArmazenamento
    
    def __init__(self, alteracaoInfosCadastro: IArmazenamento):
        self.alteracaoInfosCadastro = alteracaoInfosCadastro
        
    def __call__(self, usuario: Usuario, email: Email):
        if not(self.alteracaoInfosCadastro.usuarioExiste(usuario)):
            raise ErroUsuarioNaoExiste
        
        if email == None or email not in usuario.contato.emails:
            raise ErroEmailInvalido
        
        if email.tipo == TipoEmail.UNIVERSITARIO:
            raise ErroManipulacaoEmailFaculdade
        
        if self.alteracaoInfosCadastro.quantidadeEmails(usuario) == 1:
            raise ErroDeletarEmailUnico
        
        self.alteracaoInfosCadastro.removerEmail(usuario, email)