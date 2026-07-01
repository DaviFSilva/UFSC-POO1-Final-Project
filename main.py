from manager import TaskManager

def exibir_menu():
    print("\n" + "="*30)
    print("=== TASK MANAGER CLI ===")
    print("="*30)
    print("1. Cadastrar Usuário")
    print("2. Listar Usuários")
    print("3. Criar Tarefa")
    print("4. Listar Todas as Tarefas")
    print("5. Detalhes/Alterar Tarefa")
    print("6. Excluir Tarefa")
    print("7. Filtrar Tarefas")
    print("0. Sair")
    print("="*30)

def cadastrar_usuario_show(gerenciador):
    nome = input("Nome do usuário: ")
    email = input("Email do usuário: ")
    try:
        usuario = gerenciador.cadastrar_usuario(nome, email)
        gerenciador.salvar()
        print(f"Usuário '{usuario.nome}' cadastrado com ID {usuario.id}!")
    except ValueError as e:
        print(f"Erro: {e}")

def listar_usuarios_show(gerenciador):
    usuarios = gerenciador.listar_usuarios()
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for u in usuarios:
            print(u.exibir_detalhes())

def criar_tarefa_show(gerenciador):
    titulo = input("Título da Tarefa: ")
    descricao = input("Descrição: ")
    tarefa = gerenciador.criar_tarefa(titulo, descricao)
    gerenciador.salvar()
    print(f"Tarefa '{tarefa.titulo}' criada com ID {tarefa.id}!")

def listar_tarefas_show(gerenciador):
    tarefas = gerenciador.consultar_tarefas()
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        for t in tarefas:
            print(f"ID {t.id} - {t.titulo} [{t.status}]")

def alterar_tarefa_show(gerenciador):
    try:
        id_tarefa = int(input("Digite o ID da tarefa: "))
        tarefa = gerenciador.buscar_tarefa(id_tarefa)
        if not tarefa:
            print("Tarefa não encontrada.")
            return
        
        print("\n" + tarefa.exibir_detalhes())
        print("\nO que deseja alterar?")
        print("1. Alterar Status")
        print("2. Adicionar Responsável")
        print("3. Remover Responsável")
        print("4. Adicionar Tag")
        print("5. Remover Tag")
        print("0. Voltar")
        
        sub_opcao = input("Escolha: ")
        if sub_opcao == "1":
            novo_status = input("Novo Status (Pendente, Em Andamento, Concluída, Cancelada): ")
            tarefa.status = novo_status
            print("Status atualizado!")
        elif sub_opcao == "2":
            id_usuario = int(input("ID do Usuário responsável: "))
            usuario = gerenciador.buscar_usuario(id_usuario)
            if usuario:
                tarefa.adicionar_responsavel(usuario)
                print("Responsável adicionado!")
            else:
                print("Usuário não encontrado.")
        elif sub_opcao == "3":
            id_usuario = int(input("ID do Usuário a remover: "))
            tarefa.remover_responsavel(id_usuario)
            print("Responsável removido (se existia)!")
        elif sub_opcao == "4":
            tag = input("Nova Tag: ")
            tarefa.adicionar_tag(tag)
            print("Tag adicionada!")
        elif sub_opcao == "5":
            tag = input("Tag a remover: ")
            tarefa.remover_tag(tag)
            print("Tag removida (se existia)!")
        
        # Salva alterações feitas na tarefa
        gerenciador.salvar()
    except ValueError as e:
        print(f"Erro de entrada: {e}")

def excluir_tarefa_show(gerenciador):
    try:
        id_tarefa = int(input("Digite o ID da tarefa a ser excluída: "))
        if gerenciador.excluir_tarefa(id_tarefa):
            gerenciador.salvar()
            print("Tarefa excluída com sucesso!")
        else:
            print("Tarefa não encontrada.")
    except ValueError:
        print("ID inválido.")

def filtrar_tarefas_show(gerenciador):
    print("\nFiltrar por:")
    print("1. Status")
    print("2. Responsável")
    print("3. Tag")
    filtro = input("Escolha: ")
    
    tarefas_filtradas = []
    if filtro == "1":
        status = input("Digite o status: ")
        tarefas_filtradas = gerenciador.filtrar_por_status(status)
    elif filtro == "2":
        try:
            id_usu = int(input("Digite o ID do responsável: "))
            tarefas_filtradas = gerenciador.filtrar_por_responsavel(id_usu)
        except ValueError:
            print("ID inválido.")
    elif filtro == "3":
        tag = input("Digite a tag: ")
        tarefas_filtradas = gerenciador.filtrar_por_tag(tag)
    
    if tarefas_filtradas:
        print(f"\nEncontradas {len(tarefas_filtradas)} tarefas:")
        for t in tarefas_filtradas:
            print(t.exibir_detalhes())
    else:
        print("\nNenhuma tarefa encontrada com este filtro.")


def main():
    gerenciador = TaskManager()
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "0":
            print("Saindo do Task Manager...")
            break
        elif opcao == "1":
            cadastrar_usuario_show(gerenciador)
        elif opcao == "2":
            listar_usuarios_show(gerenciador)
        elif opcao == "3":
            criar_tarefa_show(gerenciador)
        elif opcao == "4":
            listar_tarefas_show(gerenciador)
        elif opcao == "5":
            alterar_tarefa_show(gerenciador)
        elif opcao == "6":
            excluir_tarefa_show(gerenciador)
        elif opcao == "7":
            filtrar_tarefas_show(gerenciador)
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
