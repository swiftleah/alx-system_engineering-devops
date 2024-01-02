#!/usr/bin/python3
""" this script uses REST API for a given employee ID & returns
    info about his/her TODO list & its progress """
import requests
import sys


if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(URL + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(URL + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t["title"] for t in todo if t.get("completed", False)]
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(completed), len(todo)))
    for c in completed:
        print("\t {}".format(c))
