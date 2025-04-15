from datetime import datetime

def format_task(task, show_description=False):
    """Format a task for display."""
    priority_colors = {
        "high": "\033[91m",  # Red
        "medium": "\033[93m",  # Yellow
        "low": "\033[92m",  # Green
    }
    reset = "\033[0m"
    status_symbol = "✓" if task["completed"] else " "

    # Format due date
    due_str = ""
    if task["due_date"]:
        try:
            due_date = datetime.fromisoformat(task["due_date"])
            due_str = due_date.strftime("%Y-%m-%d")

            # Check if overdue
            if not task["completed"] and due_date < datetime.now():
                due_str = f"\033[91m{due_str} (OVERDUE)\033[0m"
        except ValueError:
            due_str = task["due_date"]

    priority_color = priority_colors.get(task["priority"], reset)

    # Format the basic task line
    result = f"[{status_symbol}] {task['id'][:8]} - {priority_color}{task['title']}{reset}"
    if due_str:
        result += f" (Due: {due_str})"

    # Add description if requested
    if show_description and task["description"]:
        result += f"\n    {task['description']}"

    return result

def print_task_list(tasks, verbose=False):
    """Print a formatted list of tasks."""
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(format_task(task, verbose))

    # Print summary
    completed = sum(1 for task in tasks if task["completed"])
    print(f"\nTotal: {len(tasks)} tasks, {completed} completed, {len(tasks) - completed} pending")