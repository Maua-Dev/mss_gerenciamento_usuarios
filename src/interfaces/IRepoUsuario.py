from abc import ABC, abstractmethod
from typing import Optional
from datetime import date

from devmaua.src.models.ra import RA
from devmaua.src.models.usuario import Usuario
from devmaua.src.models.telefone import Telefone
from devmaua.src.models.email import Email
from devmaua.src.models.endereco import Endereco
from devmaua.src.models.usuario import Usuario

from devmaua.src.enum.tipo_telefone import TipoTelefone
from devmaua.src.enum.tipo_endereco import TipoEndereco
from devmaua.src.enum.tipo_email import TipoEmail




class IArmazenamento(ABC):
    """"
    Interface com os métodos necessários para o gerenciamento de usuários
    """
    @abstractmethod
    def getUsuario(self, ra: RA):
        pass

    @abstractmethod
    def cadastrarUsuario(self, usuario: Usuario):
        pass

    @abstractmethod
    def logarUsuario(self, login: str, senha: str):
        pass

    @abstractmethod
    def usuarioExiste(self, usuario_outro: Usuario):
        pass

    @abstractmethod
    def deletarUsuarioPorEmail(self, email: str):
        """ Remove um usuario a partir do seu email """
        pass

    @abstractmethod
    def usuarioExistePorEmail(self, email: str):
        """ Retorna se um usuario existe """
        pass

    @abstractmethod
    def adicionarTelefone(self, usuario: Usuario, telefone: Telefone):
        """ Adiciona um novo telefone na lista de telefones de Contato. """
        pass

    @abstractmethod
    def removerTelefone(self, usuario: Usuario, telefone: Telefone):
        """ Remove um telefone da lista de telefones de Contato. """
        pass

    @abstractmethod
    def editarTelefone(self, usuario: Usuario, telefone: Telefone, tipo: Optional[TipoTelefone], ddd: Optional[int],
                       numero: Optional[str], prioridade: Optional[int]):
        """ Edita informacoes de um Telefone"""
        pass

    @abstractmethod
    def adicionarEmail(self, usuario: Usuario, email: Email):
        """ Adiciona um novo email na lista de emails de Contato. """
        pass

    @abstractmethod
    def removerEmail(self, usuario: Usuario, email: Email):
        """ Remove um email da lista de email de Contato. """
        pass

    @abstractmethod
    def editarEmail(self, usuario: Usuario, email: Email, email_novo: Optional[str], tipo: Optional[TipoEmail],
                    prioridade: Optional[int]):
        """ Edita informacoes de um email"""
        pass

    @abstractmethod
    def adicionarEndereco(self, usuario: Usuario, endereco: Endereco):
        """ Adiciona um novo endereco na lista de enderecos de Contato. """
        pass

    @abstractmethod
    def removerEndereco(self, usuario: Usuario, endereco: Endereco):
        """ Remove um endereco da lista de enderecos de Contato. """
        pass

    @abstractmethod
    def editarEndereco(self, usuario: Usuario, endereco: Endereco, logradouro: Optional[str], numero: Optional[int],
                       cep: Optional[str], complemento: Optional[str], tipo: Optional[TipoEndereco]):
        """ Edita informacoes de um endereco"""
        pass

    @abstractmethod
    def quantidadeEmails(self, usuario: Usuario):
        """ Retorna a quantidade de emails que o usuario tem """
        pass

    @abstractmethod
    def quantidadeTelefones(self, usuario: Usuario):
        """ Retorna a quantidade de telefones que o usuario tem """
        pass

    @abstractmethod
    def quantidadeEnderecos(self, usuario: Usuario):
        """ Retorna a quantidade de enderecos que o usuario tem """
        pass

    @abstractmethod
    def usuarioExiste(self, usuario: Usuario):
        """ Retorna se um usuario existe """
        pass

    @abstractmethod
    def getUsuarioPorNomeENascimento(self, nome: str, nascimento: date):
        """ Busca um usuario pelo nome e data de nascimento """
        pass