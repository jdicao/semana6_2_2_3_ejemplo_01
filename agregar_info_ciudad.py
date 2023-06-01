"""
    Agregar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# nos conectamos a una db especifica
db = client.utpl_demo01
#seteamos para trabajar con la coleccion ciudad
coleccion = db.ciudad

# agregar documentos a la coleccion

# agregar documentos individuales con el uso de diccionarios y el metodo insert_one que nos ofrece pymongo
print("Agregando documentos individuales...\n")
data_01 = {"nombre_ciudad": "Milagro", "provincia": "Guayas", "pais":"Ecuador", "numero_habitantes": 200000, "numero_parroquias": 5}
coleccion.insert_one(data_01)
print("")
print("Documentos individuales insertados...\n")
data_02 = {"nombre_ciudad": "Duran", "provincia": "Guayas", "pais":"Ecuador", "numero_habitantes": 200000}
coleccion.insert_one(data_02)
print("")

print("Agregando varios documentos...\n")
# agregar varios documentos mediante insert_many
lista = [
         {"nombre_ciudad": "Guayaquil", "provincia": "Guayas", "pais":"Ecuador", "numero_habitantes": 3000000},
         {"nombre_ciudad": "Manta", "provincia": "Manabi", "pais":"Ecuador", "numero_habitantes": 450000}
        ]

coleccion.insert_many(lista)
print("")
print("Documentos agregados.")