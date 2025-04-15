
from datetime import datetime
from core.models import create_task


def add_task(tasks, title, description="", due_date=None, priority="medium"):
    new_task = create_task(title, description, due_date, priority)
    return tasks + [new_task]

def get_task_by_id(tasks, task_id):
    matching = [task for task in tasks if task["id"] == task_id]
    return matching[0] if matching else None

def update_task(tasks, task_id, updates):
    return [
        {**task, **updates} if task["id"] == task_id else task
        for task in tasks
    ]

def complete_task(tasks, task_id):
    return [
        {**task, "completed": True, "completed_at": datetime.now().isocalendar()}
        if task["id"] == task_id else task
        for task in tasks
    ]

def delete_task(tasks, task_id):
    return [task for task in tasks if task["id"] != task_id]

def filter_tasks(tasks, status="all", sort_by="priority"):
    if status == "pending":
        filtered = [task for task in tasks if not task["completed"]]
    elif status == "completed":
        filtered = [task for task in tasks if task["completed"]]
    else:  # "all"
        filtered = tasks

    # Then sort
    priority_values = {"high": 3, "medium": 2, "low": 1}

    if sort_by == "priority":
        return sorted(filtered, key=lambda t: (
            -priority_values.get(t["priority"], 0),
            t["due_date"] or "9999-99-99",
            t["title"]
        ))
    elif sort_by == "due":
        return sorted(filtered, key=lambda t: (
            t["due_date"] or "9999-99-99",
            -priority_values.get(t["priority"], 0),
            t["title"]
        ))
    elif sort_by == "title":
        return sorted(filtered, key=lambda t: t["title"].lower())
    else:
        return filtered