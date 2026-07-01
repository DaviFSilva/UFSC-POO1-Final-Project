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

def main():
    gerenciador = TaskManager()
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "0":
            print("Saindo do Task Manager...")
            break
            
        elif opcao == "1":
            nome = input("Nome do usuário: ")
            email = input("Email do usuário: ")
            try:
                usuario = gerenciador.cadastrar_usuario(nome, email)
                gerenciador.salvar()
                print(f"Usuário '{usuario.nome}' cadastrado com ID {usuario.id}!")
            except ValueError as e:
                print(f"Erro: {e}")
                
        elif opcao == "2":
            usuarios = gerenciador.listar_usuarios()
            if not usuarios:
                print("Nenhum usuário cadastrado.")
            else:
                for u in usuarios:
                    print(u.exibir_detalhes())
                    
        elif opcao == "3":
            titulo = input("Título da Tarefa: ")
            descricao = input("Descrição: ")
            tarefa = gerenciador.criar_tarefa(titulo, descricao)
            gerenciador.salvar()
            print(f"Tarefa '{tarefa.titulo}' criada com ID {tarefa.id}!")
            
        elif opcao == "4":
            tarefas = gerenciador.consultar_tarefas()
            if not tarefas:
                print("Nenhuma tarefa cadastrada.")
            else:
                for t in tarefas:
                    print(f"ID {t.id} - {t.titulo} [{t.status}]")
                    
        elif opcao == "5":
            try:
                id_tarefa = int(input("Digite o ID da tarefa: "))
                tarefa = gerenciador.buscar_tarefa(id_tarefa)
                if not tarefa:
                    print("Tarefa não encontrada.")
                    continue
                
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
                
        elif opcao == "6":
            try:
                id_tarefa = int(input("Digite o ID da tarefa a ser excluída: "))
                if gerenciador.excluir_tarefa(id_tarefa):
                    gerenciador.salvar()
                    print("Tarefa excluída com sucesso!")
                else:
                    print("Tarefa não encontrada.")
            except ValueError:
                print("ID inválido.")
                
        elif opcao == "7":
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
                
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
