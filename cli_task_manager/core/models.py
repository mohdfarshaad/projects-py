from datetime import datetime

from utils.helpers import random_id 

PRIORITIES = ["low", "medium", "high"]

def create_task(title , description = "" , due_date = None, priority = "medium" ):
    return {
            "id": random_id(),
            "title":title,
            "description": description,
            "priority": priority if priority in PRIORITIES else "medium",
            "due_date": due_date,
            "created_at": datetime.now().isocalendar(),
            "completed" : False,
            "completed_at": None,
        }
