from models.person import Person

class User(Person):
    def __init__(self, user_id: int, name: str, email: str):
        super().__init__(user_id, name)
        self.__email = email

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, new_email: str):
        if "@" in new_email:
            self.__email = new_email
        else:
            raise ValueError("Email inválido.")

    def show_details(self) -> str:
        base_details = super().show_details()
        return f"[USUARIO] {base_details} | Email: {self.__email}"
