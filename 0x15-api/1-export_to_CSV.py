#!/usr/bin/python3
""" this sxcript exports data in the comma-seperated value format """
import csv
import requests
import sys


if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(URL + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(URL + "todos", params={"userId": sys.argv[1]}).json()
    user_id = sys.argv[1]
    username = employee.get("username")

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todo]
