import requests
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, "api-key.txt")

with open(file_path, "r") as file:
    token = file.read()



def send_cmd():
    body = {
        "command": command
    }
    headers = {
        "server-key": token
    }
    request = requests.post("https://api.policeroleplay.community/v1/server/command", json=body, headers=headers)
    print(request)




print("Make sure that you pasted your api key into the api-key.txt file.")
api = input("What API do you want to use? 1: Run a command:")
if api == "1":
    command = input("Wha command do you want to use? Please include the prefix. (Example: :h Helle World!): ")
    print("If it writes 200 then it worked.")
    send_cmd()
else:
    print(f"{api} is not on the list.")