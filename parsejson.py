import urllib.request
import json
import socket as s

class Plant:
    def __init__(self):
        self.name = None
        self.id = None
        self.info = None
        self.habitat = None
        self.gbc = None
        self.facts = None
        self.references = None
        self.development = None

        self.access = None

    def set_all(self, json_file):
        task = json_file["task"]
        self.name = task["name"]
        self.info = task["info"]
        self.id = task["id"]

        data = self.info

        self.habitat = data["Distribution/Habitat"]
        self.gbc = data["General Botanical Characteristics"]
        self.facts = data["Interesting Facts"]
        self.references = data["References"]
        self.development = data["Seasonal Development"]

        self.access = {
            1: self.gbc,
            2: self.habitat,
            3: self.development,
            4: self.facts,
            5: self.references
        }

    def __str__(self):
        return self.name

    def view(self):
        selection = ["General Botanical Characteristics: 1",
                     "Distribution/Habitat: 2",
                     "Seasonal Development: 3",
                     "Interesting Facts: 4",
                     "References: 5",
                     "Done: done"
                     ]
        while True:
            print("Plant: ", self.name)
            for cmd in selection:
                print(cmd)
            print()
            cmd = input("What would you like to view?")
            print()
            try:
                cmd = int(cmd)
                print(self.access[cmd][0])
                print()
            except:
                if cmd == "done":
                    print("ending program")
                    break
                else:
                    continue


def get_ip():
    if s.gethostbyname(s.getfqdn()) == "127.0.0.1":
        ip = input("enter your ip address: ")
    else:
        ip = s.gethostbyname(s.getfqdn())
    return ip
ip = get_ip()
address = "http://" + ip + ":5000/1"
print(address)

url = address

response = urllib.request.urlopen(url)
str_response = response.read().decode('utf-8')
obj = json.loads(str_response)
plant = Plant()
plant.set_all(obj)
plant.view()

