import json
import os
from hashlib import sha256

STORE = "store.json"

def load_file():
    if os.path.exists(STORE):
        with open(STORE, "r") as file:
            return  json.load(file)
    else:
        return []
    
def save_file(item):
    with open (STORE, "w") as file:
        json.dump(item, file, indent=4)

def hash_password(password):
    return sha256(password.encode()).hexdigest()

def store_file():
    email = input("Enter your E-mail: ")
    password = input("Enter your password: ")
    password = hash_password(password)
    task = load_file()
    task.append({"email": email ,"password": password})
    save_file(task)

def login(email, password):
    credentials = load_file()
    for items in credentials:
        if email in items["email"] and password in items["password"]:
            return True
        else:
            return False

def main():
    selection = int(input("Please Select one:\n1. Add credential\n2. Login "))
    if selection == 1:
        store_file()
    elif selection == 2:
        email = input("Enter email: ")
        password = input("Enter password: ")
        password = hash_password(password)
        res = login(email, password)
        print(res)
    else:
        print("Wrong Selection")

if __name__ == "__main__":
    main()
