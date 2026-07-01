from models.user import User

class Task:
    def __init__(self, task_id: int, title: str, description: str):
        self.__id = task_id
        self.__title = title
        self.__description = description
        self.__status = "Pendente" 
        self.__assignees = []
        self.__tags = []

    @property
    def id(self) -> int:
        return self.__id

    @property
    def title(self) -> str:
        return self.__title

    @property
    def description(self) -> str:
        return self.__description

    @property
    def status(self) -> str:
        return self.__status

    @property
    def assignees(self) -> list:
        return list(self.__assignees)

    @property
    def tags(self) -> list:
        return list(self.__tags)

    @title.setter
    def title(self, new_title: str):
        self.__title = new_title

    @description.setter
    def description(self, new_description: str):
        self.__description = new_description

    @status.setter
    def status(self, new_status: str):
        valid_statuses = ["Pendente", "Em Andamento", "Concluída", "Cancelada"]
        if new_status in valid_statuses:
            self.__status = new_status
        else:
            raise ValueError(f"Status inválido. Escolha entre: {', '.join(valid_statuses)}")

    # Public methods
    def add_assignee(self, user: User):
        if user not in self.__assignees:
            self.__assignees.append(user)

    def remove_assignee(self, user_id: int):
        self.__assignees = [u for u in self.__assignees if u.id != user_id]

    def add_tag(self, tag: str):
        tag = tag.strip().lower()
        if tag and tag not in self.__tags:
            self.__tags.append(tag)
            
    def remove_tag(self, tag: str):
        tag = tag.strip().lower()
        if tag in self.__tags:
            self.__tags.remove(tag)

    def show_details(self) -> str:
        assignees_names = ", ".join([u.name for u in self.__assignees]) if self.__assignees else "Nenhum"
        tags_str = ", ".join(self.__tags) if self.__tags else "Nenhuma"
        
        return (f"--- Tarefa #{self.__id} ---\n"
                f"Título: {self.__title}\n"
                f"Descrição: {self.__description}\n"
                f"Status: {self.__status}\n"
                f"Responsáveis: {assignees_names}\n"
                f"Tags: {tags_str}\n"
                "---------------------")
