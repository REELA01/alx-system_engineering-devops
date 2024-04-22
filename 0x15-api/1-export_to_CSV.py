#!/usr/bin/python3
"""extend your Python script to export data in the JSON format"""
import csv
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + user
    reqq = requests.get(url_user)
    """ANYTHING"""
    user_name = reqq.json().get('username')
    task = url_user + '/todos'
    reqq = requests.get(task)
    tasks = reqq.json()
    with open('{}.csv'.format(user), 'w') as csvfile:
        for task in tasks:
            completed = task.get('completed')
            """Complete"""
            title_task = task.get('title')
            """Done"""
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user, user_name, completed, title_task))
