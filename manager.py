from models.usuario import Usuario
from models.tarefa import Tarefa
from storage import carregar_dados, salvar_dados

class TaskManager:
    def __init__(self):
        self.usuarios, self.tarefas = carregar_dados()
        self.prox_id_usuario = max(self.usuarios.keys(), default=0) + 1
        self.prox_id_tarefa = max([t.id for t in self.tarefas], default=0) + 1

    def salvar(self):
        # Chama o módulo de storage para salvar o estado atual.
        salvar_dados(self.usuarios, self.tarefas)

    # CRUD de Usuários
    def cadastrar_usuario(self, nome: str, email: str) -> Usuario:
        novo_usuario = Usuario(self.prox_id_usuario, nome, email)
        self.usuarios[novo_usuario.id] = novo_usuario
        self.prox_id_usuario += 1
        return novo_usuario

    def listar_usuarios(self) -> list:
        return list(self.usuarios.values())

    def buscar_usuario(self, id_usuario: int) -> Usuario:
        return self.usuarios.get(id_usuario)

    # CRUD de Tarefas
    def criar_tarefa(self, titulo: str, descricao: str) -> Tarefa:
        nova_tarefa = Tarefa(self.prox_id_tarefa, titulo, descricao)
        self.tarefas.append(nova_tarefa)
        self.prox_id_tarefa += 1
        return nova_tarefa

    def consultar_tarefas(self) -> list:
        return self.tarefas
        
    def buscar_tarefa(self, id_tarefa: int) -> Tarefa:
        for t in self.tarefas:
            if t.id == id_tarefa:
                return t
        return None

    def excluir_tarefa(self, id_tarefa: int) -> bool:
        tarefa = self.buscar_tarefa(id_tarefa)
        if tarefa:
            self.tarefas.remove(tarefa)
            return True
        return False

    # Filtros
    def filtrar_por_status(self, status: str) -> list:
        return [t for t in self.tarefas if t.status.lower() == status.lower()]

    def filtrar_por_responsavel(self, id_usuario: int) -> list:
        tarefas_usuario = []
        for t in self.tarefas:
            for resp in t.responsaveis:
                if resp.id == id_usuario:
                    tarefas_usuario.append(t)
                    break
        return tarefas_usuario

    def filtrar_por_tag(self, tag: str) -> list:
        return [t for t in self.tarefas if tag.lower() in t.tags]
