#!/usr/bin/python3
# Apython script that uses RESTful Api to give information about user's TO DO LIST
import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todo_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)

        user_data = user_response.json()
        todo_data = todo_response.json()

        if not user_data:
            print(f"Employee with ID {employee_id} not found.")
            return

        employee_name = user_data['name']

        total_tasks = len(todo_data)
        completed_tasks = sum(1 for task in todo_data if task['completed'])

        print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")

        for task in todo_data:
            if task['completed']:
                print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
