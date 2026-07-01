# Diagrama de Classes UML

```mermaid
classDiagram
    direction TB

    class Person {
        <<Abstract>>
        - __id: int
        - __name: str
        + id: int
        + name: str
        + show_details() str
    }

    class User {
        - __email: str
        + email: str
        + show_details() str
    }

    class Task {
        - __id: int
        - __title: str
        - __description: str
        - __status: str
        - __assignees: list~User~
        - __tags: list~str~
        + id: int
        + title: str
        + description: str
        + status: str
        + assignees: list
        + tags: list
        + add_assignee(user: User) void
        + remove_assignee(user_id: int) void
        + add_tag(tag: str) void
        + remove_tag(tag: str) void
        + show_details() str
    }

    class TaskManager {
        - usuarios: dict
        - tarefas: list
        - prox_id_usuario: int
        - prox_id_tarefa: int
        + salvar() void
        + cadastrar_usuario(nome, email) Usuario
        + listar_usuarios() list
        + buscar_usuario(id) Usuario
        + criar_tarefa(titulo, descricao) Tarefa
        + consultar_tarefas() list
        + buscar_tarefa(id) Tarefa
        + excluir_tarefa(id) bool
        + filtrar_por_status(status) list
        + filtrar_por_responsavel(id) list
        + filtrar_por_tag(tag) list
    }

    %% Relacionamentos
    Person <|-- User : Herança
    
    TaskManager *-- User : Composição
    TaskManager *-- Task : Composição
    
    Task o-- User : Agregação
```
