from models.usuario import Usuario

class Tarefa:
    def __init__(self, id_tarefa: int, titulo: str, descricao: str):
        self.__id = id_tarefa
        self.__titulo = titulo
        self.__descricao = descricao
        self.__status = "Pendente" # Status inicial padrão
        self.__responsaveis = []   # Agregação: Uma lista de objetos Usuario
        self.__tags = []           # Lista de strings

    # Getters
    @property
    def id(self) -> int:
        return self.__id

    @property
    def titulo(self) -> str:
        return self.__titulo

    @property
    def descricao(self) -> str:
        return self.__descricao

    @property
    def status(self) -> str:
        return self.__status

    @property
    def responsaveis(self) -> list:
        return list(self.__responsaveis)

    @property
    def tags(self) -> list:
        return list(self.__tags)

    # Setters
    @titulo.setter
    def titulo(self, novo_titulo: str):
        self.__titulo = novo_titulo

    @descricao.setter
    def descricao(self, nova_descricao: str):
        self.__descricao = nova_descricao

    @status.setter
    def status(self, novo_status: str):
        status_validos = ["Pendente", "Em Andamento", "Concluída", "Cancelada"]
        if novo_status in status_validos:
            self.__status = novo_status
        else:
            raise ValueError(f"Status inválido. Escolha entre: {', '.join(status_validos)}")

    # Métodos públicos
    def adicionar_responsavel(self, usuario: Usuario):
        if usuario not in self.__responsaveis:
            self.__responsaveis.append(usuario)

    def remover_responsavel(self, usuario_id: int):
        self.__responsaveis = [u for u in self.__responsaveis if u.id != usuario_id]

    def adicionar_tag(self, tag: str):
        tag = tag.strip().lower()
        if tag and tag not in self.__tags:
            self.__tags.append(tag)
            
    def remover_tag(self, tag: str):
        tag = tag.strip().lower()
        if tag in self.__tags:
            self.__tags.remove(tag)

    def exibir_detalhes(self) -> str:
        nomes_responsaveis = ", ".join([u.nome for u in self.__responsaveis]) if self.__responsaveis else "Nenhum"
        tags_str = ", ".join(self.__tags) if self.__tags else "Nenhuma"
        
        return (f"--- Tarefa #{self.__id} ---\n"
                f"Título: {self.__titulo}\n"
                f"Descrição: {self.__descricao}\n"
                f"Status: {self.__status}\n"
                f"Responsáveis: {nomes_responsaveis}\n"
                f"Tags: {tags_str}\n"
                "---------------------")
