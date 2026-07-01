import json
import os
from models.usuario import Usuario
from models.tarefa import Tarefa

DATA_FILE = "dados.json"

def salvar_dados(usuarios_dict, tarefas_list):
    dados = {
        "usuarios": [],
        "tarefas": []
    }
    
    for u in usuarios_dict.values():
        dados["usuarios"].append({
            "id": u.id,
            "nome": u.nome,
            "email": u.email
        })
        
    for t in tarefas_list:
        dados["tarefas"].append({
            "id": t.id,
            "titulo": t.titulo,
            "descricao": t.descricao,
            "status": t.status,
            "responsaveis": [u.id for u in t.responsaveis],
            "tags": t.tags
        })
        
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def carregar_dados():
    usuarios_dict = {}
    tarefas_list = []
    
    if not os.path.exists(DATA_FILE):
        return usuarios_dict, tarefas_list
        
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            dados = json.load(f)
            
            # Recriar instâncias de Usuario
            for u_dados in dados.get("usuarios", []):
                usuario = Usuario(u_dados["id"], u_dados["nome"], u_dados["email"])
                usuarios_dict[usuario.id] = usuario
                
            # Recriar instâncias de Tarefa
            for t_dados in dados.get("tarefas", []):
                tarefa = Tarefa(t_dados["id"], t_dados["titulo"], t_dados["descricao"])
                tarefa.status = t_dados["status"]
                
                for tag in t_dados.get("tags", []):
                    tarefa.adicionar_tag(tag)
                    
                for resp_id in t_dados.get("responsaveis", []):
                    if resp_id in usuarios_dict:
                        tarefa.adicionar_responsavel(usuarios_dict[resp_id])
                        
                tarefas_list.append(tarefa)
                
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Erro ao carregar os dados: {e}. Iniciando com dados vazios.")
        
    return usuarios_dict, tarefas_list
