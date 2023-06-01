"""
    Agregar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# nos conectamos a una db especifica
db = client.utpl_demo01
#seteamos para trabajar con la coleccion pais
coleccion = db.pais

# agregar documentos a la coleccion

# agregar documentos individuales con el uso de diccionarios y el metodo insert_one que nos ofrece pymongo
print("Agregando documentos individuales...\n")
data_01 = {"nombre_pais": "Ecuador", "codigo": 593, "capital":"Quito", "numero_habitantes": 17000000}
coleccion.insert_one(data_01)

data_02 = {"nombre_pais": "Paraguay", "codigo": 595, "capital":"Asuncion", "numero_habitantes": 15000000}
coleccion.insert_one(data_02)
print("Documentos individuales insertados...\n")
print("")

print("Agregando varios documentos...\n")
# agregar varios documentos mediante insert_many
lista = [
         {"nombre_pais": "Colombia", "codigo": 57, "capital":"Bogota", "numero_habitantes": 51000000},
         {"nombre_pais": "Brasil", "codigo": 55, "capital":"Brasilia", "numero_habitantes": 241000000}
        ]

coleccion.insert_many(lista)
print("")
print("Documentos agregados.")