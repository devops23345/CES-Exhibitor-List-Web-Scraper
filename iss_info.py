import os
print("Current File Name : ",os.path.realpath(__file__))


import requests



people = requests.get('http://api.open-notify.org/astros.json')
iss_position  = requests.get('http://api.open-notify.org/iss-now.json')



people_json = people.json()
iss_position_json = iss_position.json()

print("People on the ISS:")
print(people_json)
print("")
print("Current ISS Position")
print(iss_position_json)

