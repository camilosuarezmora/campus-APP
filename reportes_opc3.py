import json

with open("datos//trainers.json","r") as trainers:
    dicc_trainers = json.load(trainers)

print("==========CONOCE LOS TRAINERS==========")

print("Los trainers que se encuentran trabajando con campuslands son: ")
for profesores in dicc_trainers.keys():
    print(f"    {profesores}")