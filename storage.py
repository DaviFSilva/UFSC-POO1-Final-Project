import json
import os
from models.user import User
from models.task import Task

DATA_FILE = "data.json"

def save_data(users_dict, tasks_list):
    data = {
        "users": [],
        "tasks": []
    }
    
    for u in users_dict.values():
        data["users"].append({
            "id": u.id,
            "name": u.name,
            "email": u.email
        })
        
    for t in tasks_list:
        data["tasks"].append({
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "status": t.status,
            "assignees": [u.id for u in t.assignees],
            "tags": t.tags
        })
        
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load_data():
    users_dict = {}
    tasks_list = []
    
    if not os.path.exists(DATA_FILE):
        return users_dict, tasks_list
        
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            
            for u_data in data.get("users", []):
                user = User(u_data["id"], u_data["name"], u_data["email"])
                users_dict[user.id] = user
                
            for t_data in data.get("tasks", []):
                task = Task(t_data["id"], t_data["title"], t_data["description"])
                task.status = t_data["status"]
                
                for tag in t_data.get("tags", []):
                    task.add_tag(tag)
                    
                for assignee_id in t_data.get("assignees", []):
                    if assignee_id in users_dict:
                        task.add_assignee(users_dict[assignee_id])
                        
                tasks_list.append(task)
                
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Erro ao carregar os dados: {e}. Iniciando com dados vazios.")
        
    return users_dict, tasks_list
