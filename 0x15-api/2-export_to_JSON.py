#!/usr/bin/python3
""" this script exports in the JSON format """
import json
import requests
import sys


if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(URL + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(URL + "todos", params={"userId": sys.argv[1]}).json()
    user_id = sys.argv[1]
    username = employee.get("username")

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
             "task": t.get("title"),
             "completed": t.get("completed"),
             "username": username
            } for t in todo]}, jsonfile)
