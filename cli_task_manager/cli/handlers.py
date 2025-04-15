
from core.models import PRIORITIES
from core.operations import (
    add_task,
    get_task_by_id,
    update_task,
    complete_task,
    delete_task,
    filter_tasks
)
from core.storage import load_tasks, save_tasks
from cli.formatters import print_task_list

def handle_add(args):
    tasks = load_tasks()

    if len(args) < 1:
        print("Error: Title is required")
        return

    title = args[0]
    description = args[1] if len(args) > 1 else ""
    due_date = args[2] if len(args) > 2 else None
    priority = args[3].lower() if len(args) > 3 else "medium"

    if priority not in PRIORITIES:
        print(f"Warning: Invalid priority '{priority}'. Using 'medium' instead.")
        priority = "medium"

    updated_tasks = add_task(tasks, title, description, due_date, priority)
    
    
    if save_tasks(updated_tasks):
        print(f"Task added: {title}")

def handle_list(args):
    tasks = load_tasks()

    # Parse arguments
    status = args[0] if args and args[0] in ["pending", "completed", "all"] else "pending"
    sort_by = args[1] if len(args) > 1 and args[1] in ["priority", "due", "title"] else "priority"

    filtered_tasks = filter_tasks(tasks, status, sort_by)
    print_task_list(filtered_tasks, verbose=True)

def handle_update(args):
    if not args:
        print("Error: Task ID is required")
        return

    task_id = args[0]
    tasks = load_tasks()
    task = get_task_by_id(tasks, task_id)

    if not task:
        print(f"Error: Task with ID {task_id} not found")
        return

    updates = {}
    if len(args) > 1 and args[1]:  
        updates["title"] = args[1]
    if len(args) > 2 and args[2]: 
        updates["description"] = args[2]
    if len(args) > 3 and args[3]:
        updates["due_date"] = args[3]
    if len(args) > 4 and args[4]:
        priority = args[4].lower()
        if priority in PRIORITIES:
            updates["priority"] = priority
        else:
            print(f"Warning: Invalid priority '{priority}'. Not updating priority.")

    if not updates:
        print("No updates provided.")
        return

    updated_tasks = update_task(tasks, task_id, updates)
    if save_tasks(updated_tasks):
        print(f"Task updated: {task_id}")

def handle_complete(args):
    if not args:
        print("Error: Task ID is required")
        return

    task_id = args[0]
    tasks = load_tasks()
    task = get_task_by_id(tasks, task_id)
    
    print(task)

    if not task:
        print(f"Error: Task with ID {task_id} not found")
        return

    if task["completed"]:
        print(f"Task {task_id} is already completed")
        return

    updated_tasks = complete_task(tasks, task_id)
    if save_tasks(updated_tasks):
        print(f"Task completed: {task['title']}")

def handle_delete(args):
    if not args:
        print("Error: Task ID is required")
        return

    task_id = args[0]
    tasks = load_tasks()
    task = get_task_by_id(tasks, task_id)

    if not task:
        print(f"Error: Task with ID {task_id} not found")
        return

    confirm = input(f"Are you sure you want to delete task '{task['title']}'? (y/n): ")
    if confirm.lower() != 'y':
        print("Deletion cancelled")
        return

    updated_tasks = delete_task(tasks, task_id)
    if save_tasks(updated_tasks):
        print(f"Task deleted: {task['title']}")


def print_help():
    print("""
Task Manager -  CLI Todo App

USAGE:
  python -m task_manager.main add <title> [<description>] [<due_date:YYYY-MM-DD>] [<priority:low|medium|high>]
  python -m task_manager.main list [pending|completed|all] [priority|due|title]
  python -m task_manager.main update <id> [<title>] [<description>] [<due_date>] [<priority>]
  python -m task_manager.main complete <id>
  python -m task_manager.main delete <id>
  python -m task_manager.main help

EXAMPLES:
  python -m task_manager.main add "Fix bug in login" "The login button doesn't work" "2023-12-31" "high"
  python -m task_manager.main list pending priority
  python -m task_manager.main complete abc123

""")