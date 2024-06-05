import json
print("     CONOCE LOS CAMPERS QUE APROBARON LA PRUEBA DE INGRESO   ")

with open("datos//campers.json", "r") as campers:
    manejable = json.load(campers)
aprobaron=[]    
aprobo=False
for contenido in manejable:
    nota = manejable[contenido]["Nota_de_ingreso"]
    nombre = manejable[contenido]["Nombre"]
    if nota > 60:
        aprobo=True
        print(f"El usuario {nombre} con el documento {contenido} aprobó la prueba de ingreso con una nota de {nota}")
        