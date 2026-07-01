from models.pessoa import Pessoa

class Usuario(Pessoa):
    def __init__(self, id_usuario: int, nome: str, email: str):
        super().__init__(id_usuario, nome)
        self.__email = email

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, novo_email: str):
        if "@" in novo_email:
            self.__email = novo_email
        else:
            raise ValueError("Email inválido.")

    def exibir_detalhes(self) -> str:
        detalhes_base = super().exibir_detalhes()
        return f"[USUARIO] {detalhes_base} | Email: {self.__email}"
