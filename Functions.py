import json
from datetime import datetime
from tabulate import tabulate

# Validate date function
def validate_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Get project details
def get_project_details():
    description = input("Enter description: ").strip()
    goal = input("Enter goal: ").strip()
    if goal == "" or not goal.isdigit():
        print("Invalid goal. Must be a number.")
        return None
    start_date = input("Enter start date (YYYY-MM-DD): ").strip()
    if not validate_date(start_date):
        print("Invalid start date. Format: YYYY-MM-DD.")
        return None
    end_date = input("Enter end date (YYYY-MM-DD): ").strip()
    if not validate_date(end_date):
        print("Invalid end date. Format: YYYY-MM-DD.")
        return None
    return [description, goal, start_date, end_date]

ls = {}
try:
    with open("projects.json", "r") as f:
        ls = json.load(f)
except FileNotFoundError:
    pass

while True:
    _input = input("Create project, View Projects, Edit project, Delete project or Exit: ").strip().lower()
    if _input == "exit":
        print("Exiting the program.")
        with open("projects.json", "w") as f:
            json.dump(ls, f)
        break

    if _input == "create":
        title = input("Enter title: ").strip()
        if title == "":
            print("The title is invalid.")
            continue
        details = get_project_details()
        if details:
            ls[title] = details
            print("Project created successfully.")

    elif _input == "view":
        if ls:
            headers = ["Title", "Description", "Goal", "Start Date", "End Date"]
            data = [[title, *details] for title, details in ls.items()]
            print(tabulate(data, headers=headers, tablefmt="grid"))
        else:
            print("No projects available.")

    elif _input == "edit":
        title = input("Enter title of the project to edit: ").strip()
        if title in ls:
            details = get_project_details()
            if details:
                ls[title] = details
                print("Project edited successfully.")
        else:
            print("Project not found.")

    elif _input == "delete":
        title = input("Enter title of the project to delete: ").strip()
        if title in ls:
            del ls[title]
            print("Project deleted successfully.")
        else:
            print("Project not found.")
    else:
        print("Invalid input.")
