
import csv
import json

from fastapi import FastAPI


app = FastAPI()

@app.get("/v1/contactos")
def get_contactos():
    # Define la lista para almacenar los datos del CSV en formato JSON
    contactos_data = []

    # Abre el archivo CSV (reemplaza 'contactos.csv' con la ruta de tu archivo CSV)
    with open('contactos.csv', newline='') as csvfile:
        # Lee el archivo CSV
        reader = csv.DictReader(csvfile)
        
        # Itera a través de las filas del CSV y agrega cada fila como un diccionario a la lista
        for row in reader:
            contactos_data.append(row)

    # Codifica los datos como JSON
    contactos_json = json.dumps(contactos_data)

    # Construye la respuesta con el JSON codificado
    response = {"contactos": contactos_json}

    return response