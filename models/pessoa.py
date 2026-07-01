class Pessoa:
    """
    Classe base que representa uma pessoa.
    Demonstra o conceito de Encapsulamento.
    """
    def __init__(self, id_pessoa: int, nome: str):
        self.__id = id_pessoa
        self.__nome = nome

    # Getters
    @property
    def id(self) -> int:
        return self.__id

    @property
    def nome(self) -> str:
        return self.__nome

    # Setters
    @nome.setter
    def nome(self, novo_nome: str):
        if novo_nome:
            self.__nome = novo_nome
        else:
            raise ValueError("O nome não pode ser vazio.")

    def exibir_detalhes(self) -> str:
        """
        Método base para exibir os detalhes da pessoa.
        Será sobrescrito nas classes filhas (Polimorfismo).
        """
        return f"ID: {self.__id} | Nome: {self.__nome}"
