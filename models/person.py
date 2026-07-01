class Person:
    def __init__(self, person_id: int, name: str):
        self.__id = person_id
        self.__name = name

    # Getters
    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    # Setters
    @name.setter
    def name(self, new_name: str):
        if new_name:
            self.__name = new_name
        else:
            raise ValueError("O nome não pode ser vazio.")

    def show_details(self) -> str:
        return f"ID: {self.__id} | Nome: {self.__name}"
