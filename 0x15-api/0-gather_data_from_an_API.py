#!/usr/bin/python3
"""using this REST API, for a given employee ID, 
returns information about his/her TODO list progress."""
import requests
import sys

if __name__ == "__main__":


    if len(sys.argv) > 1:
        user_id = sys.argv[1]

        url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
        response = requests.get(url)

        todo_list_url = 'https://jsonplaceholder.typicode.com/todos'
        todo_list_data = requests.get(todo_list_url)

        if todo_list_data.status_code == 200:
            tasks = todo_list_data.json()
            user_tasks = [task for task in tasks if task['userId'] == int(user_id)]
            completed_tasks = [task['title'] for task in user_tasks if task['completed']]

            total_number_of_tasks = len(user_tasks)
            number_of_done_tasks = len(completed_tasks)

            if response.status_code == 200:
                data = response.json()
                print(f"Employee {data['name']} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):")
                for task_title in completed_tasks:
                    print(f"\t  {task_title}")
            else:
                print('Failed to retrieve user data:', response.status_code)
        else:
            print('Failed to retrieve todo list data:', todo_list_data.status_code)
    else:
        print('No user ID provided')
