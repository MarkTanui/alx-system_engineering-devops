#!/usr/bin/python3
"""Extend your Python script to export data in the CSV format"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    u_id = requests.get('https://jsonplaceholder.typicode.com/users').json()
    json_dict = {}
    for users in u_id:
        new_list = []
        USER_ID = users.get('id')
        t = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(USER_ID)).json()
        for items in t:
            new_dict = {}
            new_dict["username"] = users.get('username')
            new_dict["task"] = items.get('title')
            new_dict["completed"] = items.get('completed')
            new_list.append(new_dict)
        json_dict[USER_ID] = new_list
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(json_dict, jsonfile)
