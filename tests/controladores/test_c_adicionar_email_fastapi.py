from devmaua.src.models.erros.erro_email import ErroDadosEmailInvalidos
from devmaua.src.models.erros.erro_usuario import ErroDadosUsuarioInvalidos

from src.controladores.fastapi.c_adicionar_email_fastapi import ControllerHTTPAdicionarEmailFastAPI
from src.repositorios.mock.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
from src.usecases.uc_cadastrar_usuario import UCCadastrarUsuario

from devmaua.src.models.usuario import Usuario
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioNaoExiste


class TestControllerAdicionarEmailFastAPI():
    
    def mockDictUsuario(self):
        return {
            "nome": "Jorge Do Teste",
            "contato": {
                "telefones": [
                    {
                        "tipo": 2,
                        "numero": "99999-9999",
                        "ddd": 11,
                        "prioridade": 3
                    }
                ],
                "emails": [
                    {
                        "email": "teste@teste.com",
                        "tipo": 1,
                        "prioridade": 1
                    }
                ],
                "enderecos": [
                    {
                        "logradouro": "rua de tal",
                        "numero": 20,
                        "cep": "00000-000",
                        "complemento": None,
                        "tipo": 1
                    }
                ]
            },
            "nascimento": "1999-02-23",
            "roles": [
                9
            ]
        }
        
    def mockDictEmail(self):
        return {
                "email": "novo@email.com",
                "tipo": 2,
                "prioridade": 2
                }
    
    def mockRepositorioComUmUsuario(self) -> ArmazenamentoUsuarioVolatil:
        repositorio = ArmazenamentoUsuarioVolatil()
        cadastrador = UCCadastrarUsuario(repositorio)
        usuario = Usuario.criarUsuarioPorDict(self.mockDictUsuario())
        assert isinstance(usuario, Usuario)
        cadastrador(usuario)
        return repositorio
    
            
    def test_controller_adicionar_email_fastapi(self):
        repoVolatil = self.mockRepositorioComUmUsuario()
        controllerAdicionarEmailFastAPI = ControllerHTTPAdicionarEmailFastAPI(repoVolatil)
        
        usuario = self.mockDictUsuario()
        email = self.mockDictEmail()
        body = {
                "usuario": usuario,
                "email": email            
                }
        response = controllerAdicionarEmailFastAPI(body = body)

        assert response.status_code == 200
        
    def test_erro_usuario_inexistente(self):
        repoVolatil = ArmazenamentoUsuarioVolatil()
        controllerAdicionarEmailFastAPI = ControllerHTTPAdicionarEmailFastAPI(repoVolatil)
        
        usuario = self.mockDictUsuario()
        email = self.mockDictEmail()
        body = {
                "usuario": usuario,
                "email": email            
                }
        response = controllerAdicionarEmailFastAPI(body = body)
        assert response.body.decode() == str(ErroUsuarioNaoExiste())
        assert response.status_code == 404
        
    def test_erro_email_invalido(self):
        repoVolatil = self.mockRepositorioComUmUsuario()
        controllerAdicionarEmailFastAPI = ControllerHTTPAdicionarEmailFastAPI(repoVolatil)
        
        usuario = self.mockDictUsuario()
        email = self.mockDictEmail()
        body = {
                "usuario": usuario,
                "email": {
                        "email": None,
                        "tipo": 2,
                        "prioridade": 2
                        }
           
                }
        response = controllerAdicionarEmailFastAPI(body = body)
        assert response.body.decode() == str(ErroDadosEmailInvalidos())
        assert response.status_code == 400
        
    def test_erro_email_vazio(self):
        repoVolatil = self.mockRepositorioComUmUsuario()
        controllerAdicionarEmailFastAPI = ControllerHTTPAdicionarEmailFastAPI(repoVolatil)
        
        usuario = self.mockDictUsuario()
        email = self.mockDictEmail()
        body = {
                "usuario": usuario,
                "email": None
                }
        response = controllerAdicionarEmailFastAPI(body = body)
        assert response.body.decode() == str(ErroDadosEmailInvalidos())
        assert response.status_code == 400
        
    def test_erro_usuario_vazio(self):
        repoVolatil = self.mockRepositorioComUmUsuario()
        controllerAdicionarEmailFastAPI = ControllerHTTPAdicionarEmailFastAPI(repoVolatil)
        
        usuario = self.mockDictUsuario()
        email = self.mockDictEmail()
        body = {
                "usuario": None,
                "email": {
                        "email": None,
                        "tipo": 2,
                        "prioridade": 2
                        }
                }
        response = controllerAdicionarEmailFastAPI(body = body)
        assert response.body.decode() == str(ErroDadosUsuarioInvalidos())
        assert response.status_code == 400
