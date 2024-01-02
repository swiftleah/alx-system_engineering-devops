#!/usr/bin/python3
""" this task exports data in the JSON format """
import json
import requests


if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(URL + "users").json()


    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(URL + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in employee}, jsonfile)
