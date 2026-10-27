tasks = [
    {"title": "Learn Git history rewriting", "completed": False},
    {"title": "Practice interactive rebase", "completed": False},
    {"title": "Understand commit squashing", "completed": False},
]


def display_tasks():
    print("Task Tracker")
    print("------------")

    for task in tasks:
        status = "Done" if task["completed"] else "Pending"
        print(f"- {task['title']} [{status}]")


def count_tasks():
    return len(tasks)


def filter_tasks(keyword):
    return [task for task in tasks if keyword.lower() in task["title"].lower()]


if __name__ == "__main__":
    display_tasks()
    print(f"\nTotal tasks in tracker: {count_tasks()}")

    print("\nTasks matching 'Git'(case-insensitive):")
    for task in filter_tasks("Git"):
        print(f"- {task['title']}")
