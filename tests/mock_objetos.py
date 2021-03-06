from devmaua.src.models.contato import Contato
from devmaua.src.models.email import Email
from devmaua.src.models.endereco import Endereco
from devmaua.src.models.telefone import Telefone
from devmaua.src.models.usuario import Usuario

from devmaua.src.enum.roles import Roles
from devmaua.src.enum.tipo_email import TipoEmail
from devmaua.src.enum.tipo_endereco import TipoEndereco
from devmaua.src.enum.tipo_telefone import TipoTelefone

import datetime


def mockUsuario() -> Usuario:
    email = Email(email='teste@teste.com',
                  tipo=TipoEmail.PRIVADO,
                  prioridade=1)
    end = Endereco(logradouro='rua de tal',
                   numero=20,
                   cep='00000-000',
                   tipo=TipoEndereco.RESIDENCIAL)
    tel = Telefone(tipo=TipoTelefone.PRIVADO,
                   numero='99999-9999',
                   ddd=11,
                   prioridade=3)
    contato = Contato(emails=[email],
                      telefones=[tel],
                      enderecos=[end])

    return Usuario(nome='jorge do teste',
                   contato=contato,
                   nascimento=datetime.date(1999, 2, 23),
                   roles=[Roles.ALUNO])

# ====== Mocks específicos - para ter um diferente do usuario ========


def mockEmail() -> Email:
    return Email(email='email@mail.com',
                 tipo=TipoEmail.TRABALHO,
                 prioridade=2)


def mockEndereco() -> Endereco:
    return Endereco(logradouro='outra rua',
                    numero=210,
                    cep='00000-098',
                    tipo=TipoEndereco.TRABALHO)


def mockTelefone() -> Telefone:
    return Telefone(tipo=TipoTelefone.TRABALHO,
                    numero='2222-2222',
                    ddd=11,
                    prioridade=3)
