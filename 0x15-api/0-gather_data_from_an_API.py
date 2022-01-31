#!/usr/bin/python3
"""
Uses a REST-API to return information of employees about their todo lists.
"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    """Get employee name"""
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(argv[1])).json()
    EMPLOYEE_NAME = r.get('name')

    """Gets tasks completed"""
    t = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                     .format(argv[1])).json()

    NUMBER_OF_DONE_TASKS = TASKS_NOT_DONE = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []
    for key in t:
        if key.get('completed') is True:
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(key.get('title'))
        elif key.get('completed') is False:
            TASKS_NOT_DONE += 1
        TOTAL_NUMBER_OF_TASKS = NUMBER_OF_DONE_TASKS + TASKS_NOT_DONE
    print('Employee {} is done with tasks({}/{}):'
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for element in TASK_TITLE:
        print("\t {}" .format(element))
