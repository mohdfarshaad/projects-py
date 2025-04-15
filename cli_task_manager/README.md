# Command Line Task Manager 📋✅

A lightweight, terminal-based task management system with persistent storage.

## Features ✨

- ✅ **Task Management**
  - Add, list, update, complete, and delete tasks
  - Set priorities (low, medium, high)
  - Add due dates and descriptions
- 📁 **Persistent Storage**
  - Automatic saving to JSON file
  - Data preserved between sessions
- 🛠 **Input Validation**
  - Date format enforcement (YYYY-MM-DD)
  - Priority level validation
  - Field sanitization

## Installation ⚙️

```bash
git clone https://github.com/yourusername/cli-task-manager.git
cd cli-task-manager
```

## Usage 🚀

### Basic Commands

```bash
# Add a new task
python main.py add "Finish project" "Write documentation" "2023-12-15" high

# List all tasks
python main.py list

# Complete a task
python main.py complete <task_id>

# Update a task
python main.py update <task_id> --title "New title" --priority medium

# Delete a task
python main.py delete <task_id>

# Show help
python main.py help
```

### Advanced Options

```bash
# Filter tasks by status
python main.py list --completed
python main.py list --pending
```

## Project Structure 🏗️

```bash

cli-task-manager/
├── core/               # Business logic
│  ├── storage.py      # Storage using json
│   ├── operations.py   # CRUD operations
│   └── models.py       # Task data model
├── cli/                # Command line interface
│   ├── handlers.py     # Command handlers
│   └── formatters.py   # Output formatting
├── main.py             # Entry point
└── tasks.json          # Task storage
```


## Contributing 🤝

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
