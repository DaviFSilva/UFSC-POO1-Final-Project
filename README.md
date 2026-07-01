# Gerenciador de Tarefas

Este projeto é uma aplicação de gerenciamento de tarefas que demonstra conceitos fundamentais de Programação Orientada a Objetos (POO), como **Herança**, **Composição**, **Agregação**, **Encapsulamento** e **Polimorfismo**.

## Funcionalidades

- **Gerenciamento de Usuários**: Cadastro e listagem de usuários.
- **Gerenciamento de Tarefas**: Criação, visualização, edição e exclusão de tarefas.
- **Tags**: Categorização de tarefas com múltiplas tags.
- **Atribuição de Responsáveis**: Associação de tarefas a usuários específicos.
- **Persistência de Dados**: Salva e carrega o estado da aplicação automaticamente.
- **Filtros**: Filtragem de tarefas por status, responsável e tags.

## Requisitos

- Python 3.12 ou superior.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/DaviFSilva/UFSC-POO1-Final-Project.git
   cd UFSC-POO1-Final-Project
   ```

2. Execute a aplicação:
   ```bash
   python3 main.py
   ```

## Estrutura do Projeto

```
.gitignore              # Arquivos ignorados pelo Git
main.py                 # Ponto de entrada da aplicação
storage.py              # Módulo de persistência de dados
data.json               # Banco de dados em JSON
manager.py              # Lógica de gerenciamento (TaskManager)
models/                 # Modelos de dados (Objetos)
├── person.py           # Classe base Person
├── user.py             # Classe User (Herda de Person)
└── task.py             # Classe Task
diagrama_classes.md     # Diagrama UML das classes
```

## Conceitos de POO Demonstrados

### Herança
- A classe `User` herda atributos e métodos da classe base `Person`.

### Encapsulamento
- Atributos privados (ex: `__name`, `__email`) protegidos por getters e setters.

### Composição
- `TaskManager` é composto por `dict` de usuários e `list` de tarefas.

### Agregação
- `Task` agrega múltiplos `User` como responsáveis.

### Polimorfismo
- Método `show_details()` sobrescrito em `User`.
