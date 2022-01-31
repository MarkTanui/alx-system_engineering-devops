#!/usr/bin/python3
"""Extend your Python script to export data in the CSV format"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    """Gets the name with the argument passed"""
    #  if type(argv[1]) == int:
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(argv[1])).json()
    USER_ID = r.get('id')
    """Gets tasks accomplished"""
    t = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                     .format(argv[1])).json()
    # now we will open a file for writing
    # create the csv writer object
    new_list = []
    for key in t:
        new_dict = {}
        new_dict["task"] = key.get('title')
        new_dict["completed"] = key.get('completed')
        new_dict["username"] = r.get('username')
        new_list.append(new_dict)
    json_dict = {}
    json_dict[USER_ID] = new_list
    with open("{}.json".format(USER_ID), 'w') as jsonfile:
        json.dump(json_dict, jsonfile)
