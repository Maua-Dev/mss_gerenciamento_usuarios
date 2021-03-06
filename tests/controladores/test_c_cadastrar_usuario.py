from src.controladores.fastapi.c_cadastrar_usuario import ControllerHTTPCadastrarUsuario
from src.repositorios.mock.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil


class TestControllerCadastrarUsuario():
    repoVolatil = ArmazenamentoUsuarioVolatil()
    controllerCadastrarUsuario = ControllerHTTPCadastrarUsuario(repoVolatil)

    def mockUsuario(self):
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

    def test_controller_cadastrar_usuario(self):
        usuario = self.mockUsuario()
        response = self.controllerCadastrarUsuario(body=usuario)
        print(response)
        print(dir(response))

        assert response.status_code == 200

    def test_controller_cadastrar_sem_nome(self):
        usuario = self.mockUsuario()
        usuario['nome'] = None
        response = self.controllerCadastrarUsuario(body=usuario)

        assert response.status_code == 400

