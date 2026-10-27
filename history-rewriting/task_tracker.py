tasks = [
    "Learn Git history rewriting",
    "Practice interactive rebase",
    "Understand commit squashing",
]

def display_tasks():
    print("Task Tracker")
    print("------------")

    for task in tasks:
        print(f"- {task}")


if __name__ == "__main__":
    display_tasks()