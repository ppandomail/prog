import json

dicc = {'nombre': 'pablo', 'edad':38, 'domicilio': {'loc': 'Capilla del Señor', 'pcia': 'Bs. As.'}}
print(dicc)
print(json.dumps(dicc)) # converte json a string