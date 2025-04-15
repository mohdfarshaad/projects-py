import math
import random
import string


def validate_date_format(date_string):
    """Validate that a string is in YYYY-MM-DD format."""
    if not date_string:
        return True

    try:
        from datetime import datetime
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    
def random_id(length = 5):
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=length))
