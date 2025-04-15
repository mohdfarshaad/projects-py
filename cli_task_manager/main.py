
import sys
from cli.handlers import (
    handle_add,
    handle_list,
    handle_update,
    handle_complete,
    handle_delete,
    print_help
)

def main():
    """Main entry point for the application."""
    if len(sys.argv) < 2:
        print_help()
        return

    command = sys.argv[1].lower()
    args = sys.argv[2:]

    # Route to the appropriate handler
    if command == "add":
        handle_add(args)
    elif command == "list":
        handle_list(args)
    elif command == "update":
        handle_update(args)
    elif command == "complete":
        handle_complete(args)
    elif command == "delete":
        handle_delete(args)
    elif command == "help":
        print_help()
    else:
        print(f"Unknown command: {command}")
        print_help()

if __name__ == "__main__":
    main()