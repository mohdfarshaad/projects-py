import json
import os.path
from shutil import which

DATA_FILE = os.path.join("core", "data", "tasks.json")

def load_tasks():
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as file:
                return json.load(file)
        else:
            return []
    except json.JSONDecodeError as e :
        print("Error: Invalid JSON in tasks file. Returning empty list.")
        return [] 
    except Exception as e:
        print(f"Error loading task: {e}")
        return []                   

def save_tasks(tasks):
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(tasks, file, indent=2)
            return True
    except Exception as e:
        print(f"Error saving tasks : {e}")
        return False
 