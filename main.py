from manager import TaskManager

def show_menu():
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

def register_user_show(manager):
    name = input("Nome do usuário: ")
    email = input("Email do usuário: ")
    try:
        user = manager.register_user(name, email)
        manager.save()
        print(f"Usuário '{user.name}' cadastrado com ID {user.id}!")
    except ValueError as e:
        print(f"Erro: {e}")

def list_users_show(manager):
    users = manager.list_users()
    if not users:
        print("Nenhum usuário cadastrado.")
    else:
        for u in users:
            print(u.show_details())

def create_task_show(manager):
    title = input("Título da Tarefa: ")
    description = input("Descrição: ")
    task = manager.create_task(title, description)
    manager.save()
    print(f"Tarefa '{task.title}' criada com ID {task.id}!")

def list_tasks_show(manager):
    tasks = manager.get_all_tasks()
    if not tasks:
        print("Nenhuma tarefa cadastrada.")
    else:
        for t in tasks:
            print(f"ID {t.id} - {t.title} [{t.status}]")

def update_task_show(manager):
    try:
        task_id = int(input("Digite o ID da tarefa: "))
        task = manager.get_task(task_id)
        if not task:
            print("Tarefa não encontrada.")
            return
        
        print("\n" + task.show_details())
        print("\nO que deseja alterar?")
        print("1. Alterar Status")
        print("2. Adicionar Responsável")
        print("3. Remover Responsável")
        print("4. Adicionar Tag")
        print("5. Remover Tag")
        print("0. Voltar")
        
        sub_option = input("Escolha: ")
        if sub_option == "1":
            new_status = input("Novo Status (Pendente, Em Andamento, Concluída, Cancelada): ")
            task.status = new_status
            print("Status atualizado!")
        elif sub_option == "2":
            user_id = int(input("ID do Usuário responsável: "))
            user = manager.get_user(user_id)
            if user:
                task.add_assignee(user)
                print("Responsável adicionado!")
            else:
                print("Usuário não encontrado.")
        elif sub_option == "3":
            user_id = int(input("ID do Usuário a remover: "))
            task.remove_assignee(user_id)
            print("Responsável removido (se existia)!")
        elif sub_option == "4":
            tag = input("Nova Tag: ")
            task.add_tag(tag)
            print("Tag adicionada!")
        elif sub_option == "5":
            tag = input("Tag a remover: ")
            task.remove_tag(tag)
            print("Tag removida (se existia)!")
        
        manager.save()
    except ValueError as e:
        print(f"Erro de entrada: {e}")

def delete_task_show(manager):
    try:
        task_id = int(input("Digite o ID da tarefa a ser excluída: "))
        if manager.delete_task(task_id):
            manager.save()
            print("Tarefa excluída com sucesso!")
        else:
            print("Tarefa não encontrada.")
    except ValueError:
        print("ID inválido.")

def filter_tasks_show(manager):
    print("\nFiltrar por:")
    print("1. Status")
    print("2. Responsável")
    print("3. Tag")
    filter_type = input("Escolha: ")
    
    filtered_tasks = []
    if filter_type == "1":
        status = input("Digite o status: ")
        filtered_tasks = manager.filter_by_status(status)
    elif filter_type == "2":
        try:
            user_id = int(input("Digite o ID do responsável: "))
            filtered_tasks = manager.filter_by_assignee(user_id)
        except ValueError:
            print("ID inválido.")
    elif filter_type == "3":
        tag = input("Digite a tag: ")
        filtered_tasks = manager.filter_by_tag(tag)
    
    if filtered_tasks:
        print(f"\nEncontradas {len(filtered_tasks)} tarefas:")
        for t in filtered_tasks:
            print(t.show_details())
    else:
        print("\nNenhuma tarefa encontrada com este filtro.")


def main():
    manager = TaskManager()
    
    while True:
        show_menu()
        option = input("Escolha uma opção: ")
        
        if option == "0":
            print("Saindo do Task Manager...")
            break
        elif option == "1":
            register_user_show(manager)
        elif option == "2":
            list_users_show(manager)
        elif option == "3":
            create_task_show(manager)
        elif option == "4":
            list_tasks_show(manager)
        elif option == "5":
            update_task_show(manager)
        elif option == "6":
            delete_task_show(manager)
        elif option == "7":
            filter_tasks_show(manager)
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
