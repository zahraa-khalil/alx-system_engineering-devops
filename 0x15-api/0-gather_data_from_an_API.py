#!/usr/bin/python3
"""Using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_id = sys.argv[1]

        base_url = 'https://jsonplaceholder.typicode.com'
        user_url = f'{base_url}/users/{user_id}'
        todos_url = f'{base_url}/todos'

        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        if todos_response.status_code == 200:
            todos = todos_response.json()
            user_todos = [todo for todo in todos
                          if todo['userId'] == int(user_id)]
            completed = [todo['title'] for todo in user_todos
                         if todo['completed']]

            total_tasks = len(user_todos)
            done_tasks = len(completed)

            if user_response.status_code == 200:
                user_data = user_response.json()
                employee_info = (f"Employee {user_data['name']} is done with "
                                 f"tasks ({done_tasks}/{total_tasks}):")
                print(employee_info)
                for title in completed:
                    print(f"\t  {title}")
            else:
                print('Failed to retrieve user data:',
                      user_response.status_code)
        else:
            print('Failed to retrieve todo list data:',
                  todos_response.status_code)
    else:
        print('No user ID provided')
